import argparse
import pandas as pd
import pickle
import os
from flask import Flask, render_template, request

def load_model(file_name):
    f = open(file_name, 'rb')
    unpickler = pickle.Unpickler(f)
    model = unpickler.load()
    f.close()
    return model
    
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# laod models
base_dir = os.path.abspath(os.path.dirname(__file__))
color_label_encoder = load_model(f"{base_dir}/models/colorFeatureLabelEncoder.pkl")
clarity_label_encoder = load_model(f"{base_dir}/models/clarityFeatureLabelEncoder.pkl")
scaler = load_model(f"{base_dir}/models/scaler.pkl")
model = load_model(f"{base_dir}/models/model.pkl")
label_encoder = load_model(f"{base_dir}/models/labelEncoder.pkl")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    params = request.form.to_dict()
    print(params)

    
    df = pd.DataFrame(params, index=[1])
    print(df)
    num_cols = df.columns.tolist()
    print(num_cols)
    # remove categorical columns
    cat_cols = ['color', 'clarity']
    for col in cat_cols:
        num_cols.remove(col)
        
    df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

    # prepare data
    
    df['color'] = color_label_encoder.transform(df['color'])
    df['clarity'] = clarity_label_encoder.transform(df['clarity'])
    
    df[df.columns] = scaler.transform(df[df.columns])
    
    target = model.predict(df)
    
    label = label_encoder.inverse_transform(target)
        
    
    return render_template('predict.html', target=label[0] )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
