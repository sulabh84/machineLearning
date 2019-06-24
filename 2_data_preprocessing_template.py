# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:46:13 2019

@author: sulabh
"""

#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
dataset = pd.read_csv('C:\sulabh\courses\machine learning\P14-Machine-Learning-AZ-Template-Folder\Part 1 - Data Preprocessing\Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)

# Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""