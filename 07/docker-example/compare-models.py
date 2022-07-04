#!/usr/bin/env python
import pandas as pd
import numpy as np
import os
import pickle

from comet_ml import Experiment
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.metrics import roc_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier



COMET_API_KEY = os.environ.get("COMET_API_KEY")
COMET_WORKSPACE = os.environ.get("COMET_WORKSPACE")
COMET_PROJECT = os.environ.get("COMET_PROJECT")


def set_target(x):
    golden_set = ['Ideal', 'Premium', 'Very Good']
    if x in golden_set:
        return 'Gold'
    return 'Silver'

def compute_metrics(y_pred, y_true):
    metrics = {}
    metrics['precision'] = precision_score(y_true, y_pred)
    metrics['recall'] = recall_score(y_true, y_pred)
    metrics['f1-score'] = f1_score(y_true, y_pred)
    metrics['accuracy'] =  accuracy_score(y_true, y_pred)
    return metrics

def save_file_to_comet(obj, obj_name, file_name, experiment):
    with open(file_name, 'wb') as file:  
        pickle.dump(obj, file)
    file.close()
    experiment.log_model(obj_name, file_name)
    
def run_experiment(ModelClass, name, feature_label_encoder_dict, scaler,label_encoder):
    experiment = Experiment(
        api_key=COMET_API_KEY,
        project_name=COMET_PROJECT,
        workspace=COMET_WORKSPACE,
    )
    experiment.set_name(name)
    experiment.add_tag(name)

    if feature_label_encoder_dict:
        for k,v in feature_label_encoder_dict.items():
            obj_name = f"{k}FeatureLabelEncoder"
            file_name = f"{obj_name}.pkl"
            save_file_to_comet(feature_label_encoder_dict[k], obj_name, file_name, experiment)
    
    if label_encoder:
        obj_name = "labelEncoder"
        file_name = f"{obj_name}.pkl"
        save_file_to_comet(label_encoder, obj_name, file_name, experiment)
    
    if scaler:
        obj_name = "scaler"
        file_name = f"{obj_name}.pkl"
        save_file_to_comet(scaler, obj_name, file_name, experiment)


    model = ModelClass()
    with experiment.train():    
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_train)
        metrics = compute_metrics(y_pred, y_train)
        experiment.log_metrics(metrics)
        experiment.log_confusion_matrix(y_train, y_pred)
        
        file_name = 'model.pkl'
        save_file_to_comet(model, name, file_name, experiment)
            
    
    with experiment.validate():
        y_pred = model.predict(X_test)
        metrics = compute_metrics(y_pred, y_test)
        experiment.log_metrics(metrics)
        experiment.log_confusion_matrix(y_test, y_pred)
        fpr, tpr, _ = roc_curve(y_test, y_pred)
        experiment.log_curve(name, fpr, tpr)
        
    
    

if __name__ == "__main__":
    df = pd.read_csv('source/diamonds.csv')
    df = df.drop(["Unnamed: 0"], axis=1)

    df['target'] = df['cut'].apply(lambda x: set_target(x))
    df.drop("cut", axis = 1,inplace=True)
    X = df.drop("target", axis = 1)
    y = df["target"]

    categories = (X.dtypes =="object")
    cat_cols = list(categories[categories].index)
    
    feature_label_encoder_dict = {}
    for col in cat_cols:
        feature_label_encoder_dict[col] = LabelEncoder()
        X[col] = feature_label_encoder_dict[col].fit_transform(X[col])
    

    scaler = StandardScaler()
    X[X.columns] = scaler.fit_transform(X[X.columns])

    
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    # for the first model also save preprocessing data
    run_experiment(RandomForestClassifier, 'RandomForest', feature_label_encoder_dict, scaler,label_encoder)
    run_experiment(DecisionTreeClassifier, 'DecisionTreeClassifier',feature_label_encoder_dict, scaler,label_encoder)
    run_experiment(GaussianNB, 'GaussianNB',feature_label_encoder_dict, scaler,label_encoder)
    run_experiment(KNeighborsClassifier, 'KNeighborsClassifier',feature_label_encoder_dict, scaler,label_encoder)
