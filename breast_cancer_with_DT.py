# -*- coding: utf-8 -*-
"""Breast cancer with DT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nhIzXyZQTWK6Y37aNU5KUVSyRtr45Z2P
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("breast_cancer_data.csv")
dataset.head()

dataset.drop(['id','Unnamed: 32'],axis = 1,inplace = True)

dataset.head()

x = dataset.drop('diagnosis',axis = 1)

x.head()

dataset.diagnosis.replace(['M','B'],[1,0],inplace = True)

y = dataset.diagnosis
y.head()

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 100)

x_train.shape

from sklearn.tree import DecisionTreeClassifier
def train_using_gini(x_train,x_test, y_train):
  clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 3, min_samples_leaf = 5)
  clf_gini.fit(x_train,y_train)
  return clf_gini

def train_using_entropy(X_train, X_test, y_train):
  clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth = 3, min_samples_leaf = 5)
  clf_entropy.fit(x_train,y_train)
  return clf_entropy

def prediction(x_test,clf_object):
  y_pred = clf_object.predict(x_test)
  print(y_pred)
  return y_pred

# calculating accuracy
from sklearn.metrics import confusion_matrix
def cal_accuracy(y_test,y_pred):
  print("accuracy score is: ", accuracy_score(y_test,y_pred),"\n")

  print("confusion matrix is: \n",confusion_matrix(y_test,y_pred),"\n")

  print("Report:\n", classification_report(y_test,y_pred),"\n")

clf_gini = train_using_gini(x_train,x_test,y_train)
clf_entropy = train_using_entropy(x_train,x_test,y_train)
print("Results using Gini Index:\n")
y_pred_gini = prediction(x_test,clf_gini)
cal_accuracy(y_test,y_pred_gini)
print("Results using Entropy:\n")
y_pred_entropy = prediction(x_test,clf_entropy)
cal_accuracy(y_test,y_pred_entropy)