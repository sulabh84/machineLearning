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

# Taking care of Missing Data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

