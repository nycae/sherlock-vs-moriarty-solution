#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy.stats import randint as sp_randint
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


path_train                  =           "model/data_train.csv"
path_test                   =           "model/data_test.csv"
path_mergered               =           "data/data_merged.csv"


def read_dataset(path):
    return pd.read_csv(path)

def to_csv(path,dataframe):
    np.savetxt(path, dataframe, delimiter=",")
    
def extract_information(df_merged, train, test):
    
    features = spy.columns[1:]
    x_train = train[features]
    y_train = train['CLASS']
    
    x_test = test[features]
    y_test = test['CLASS']
    
    X, y = x_train, y_train
    #return something
    return X,y


def report(results, n_top=3): # Función para mostrar resultados
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")

def random_forest():
    clf = RandomForestClassifier(n_estimators=512, n_jobs=-1)
    param_dist = {"max_depth": [10,9,8,7,6,5,4,3,2,None],
              "max_features": sp_randint(1, 18),
              "min_samples_split": sp_randint(2, 95),
              "min_samples_leaf": sp_randint(1, 95),
              "bootstrap": [True, False], 'class_weight':['balanced', None],
              "criterion": ["gini", "entropy"]}
    
    random_search = RandomizedSearchCV(clf, scoring= 'f1_micro', 
                                   param_distributions=param_dist, 
                                   n_iter= 80)
    
    random_search.fit(X, y)
    
    report(random_search.cv_results_)
    
    """### Execution"""

    clf_rf = RandomForestClassifier(n_estimators = 512, criterion = 'gini', 
                                    max_depth=5, max_features = 17, 
                                    min_samples_leaf = 75, min_samples_split = 39,
                                    bootstrap=True, n_jobs=-1, 
                                    class_weight=None)
    
    clf_rf.fit(x_train, y_train) # Construcción del modelo
    
    preds_rf = clf_rf.predict(x_test) # Test del modelo
    
    """### Results"""
    
    
    
    print("Random Forest: \n" 
          +classification_report(y_true=test['CLASS'], y_pred=preds_rf))
    
    # Matriz de confusión
    
    print("Matriz de confusión:\n")
    matriz = pd.crosstab(test['CLASS'], preds_rf, rownames=['actual'], colnames=['preds'])
    print(matriz)
    
    # Variables relevantes
    
    print("Relevancia de variables:\n")
    print(pd.DataFrame({'Indicador': features ,
                  'Relevancia': clf_rf.feature_importances_}),"\n")
    print("Máxima relevancia RF :" , max(clf_rf.feature_importances_), "\n")
    

if __name__ == '__main__':
    random_forest()
    
    