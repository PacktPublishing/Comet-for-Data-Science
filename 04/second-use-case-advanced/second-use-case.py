#!/usr/bin/env python
# coding: utf-8

# # Second Use Case - Advanced
# 
# ## Creating and configuring the Optmizer

import numpy as np
from comet_ml import Optimizer
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error


params = {  
   'n_estimators':{
       "type"         : "integer",
       "scalingType"  : "linear",
       "min"          : 100,
       "max"          : 110
    },
    'max_depth':{
       "type"         : "integer",
       "scalingType"  : "linear",
       "min"          : 4,
       "max"          : 6
    },
   'loss': {
       "type"         : "categorical",
       "values"       : ['squared_error', 'absolute_error']
   }
}


config = {
    "algorithm": "grid",
    "spec": {
       "maxCombo": 0,
       "objective": "minimize",
       "metric": "loss",
       "minSampleSize": 100,
       "retryLimit": 20,
       "retryAssignLimit": 0,
    },
   "trials": 1,
   "parameters": params,
   "name": "GB Optiimzer"
}


opt = Optimizer(config)

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target


n = 51
seed_list = np.arange(0, n, step = 5)

for experiment in opt.get_experiments():
    model = GradientBoostingRegressor(
          n_estimators=experiment.get_parameter("n_estimators"),
          max_depth=experiment.get_parameter("max_depth"),
          loss=experiment.get_parameter("loss"),
    )
      
    for seed in seed_list:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=seed)
        
        loss = model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test,y_pred)
        experiment.log_metric("MSE", mse, step=seed)
    