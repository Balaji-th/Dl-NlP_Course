# -*- coding: utf-8 -*-
"""Titanic_kerasTuner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VAPvGHwvMAqX7Ar2eNn6h9lHsbyl4klm

# Part 1 - Data Preprocessing
"""

!pip install -U keras-tuner

# Importing the libraries
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from kerastuner.tuners import RandomSearch

# importing the data
data = pd.read_csv('/titanic_data.csv')
data.head()

#---[ Check the Null values Column vice ]---
data.isnull().sum()

data = data.drop(['Cabin'],axis=1)
data = data.dropna()
#---[ Check the Null values Column vice ]---
data.isnull().sum()

x = data.drop(['PassengerId','Survived','Name','Ticket'],axis=1)
y = data['Survived']
x.head()

sex = pd.get_dummies(x['Sex'])
embarked = pd.get_dummies(x['Embarked'])
x = pd.concat([x,sex,embarked],axis=1)
x = x.drop(['Sex','Embarked'],axis=1)
x

data_len,feature_size = x.shape
x.shape

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

"""# Part 2 - Now let's make the ANN"""

def build_model(hp):
    model = Sequential()
    for i in range(hp.Int('num_layer',min_value=2,max_value=15)):
        model.add(Dense(units=hp.Int('units '+str(i),
                                     min_value=5,
                                     max_value=15,
                                     step=2),
                        activation='relu',kernel_initializer='he_uniform'))
    #model.add(Dense(1, activation='sigmoid'))
    model.add(Dense(1,activation='sigmoid',kernel_initializer='glorot_uniform'))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

tuner_model = RandomSearch(build_model,
                          objective = 'val_accuracy',
                          max_trials = 5,
                          executions_per_trial = 3,
                          directory='project3',
                          project_name = 'Titanic_data')
tuner_model.search_space_summary()

tuner_model.search(x_train,y_train,
             validation_data=(x_test,y_test),
             epochs=100)

tuner_model.results_summary()


