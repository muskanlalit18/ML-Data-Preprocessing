# -*- coding: utf-8 -*-

# data pre processing

#importing libraries#

#for mathematical calculations
import numpy as np 
# for plotting graphs
import matplotlib.pyplot as plt
#for importing data sets and managing them
import pandas as pd

#we have to set the working directory#

#importing dataset#

dataset=pd.read_csv('Data.csv')
#creating an independent variable matrix
X=dataset.iloc[:,:-1].values
#creating a dependent variable vector
y=dataset.iloc[:,3].values

#taking care of missing data#

from sklearn.preprocessing import Imputer
#press ctrl+I for user guide and cleaer understanding
imputer= Imputer(missing_values='NaN', strategy='mean' , axis=0)
#[:,1:3] upper bound is not included so columns actually included=1,2
imputer=imputer.fit(X[:, 1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

#encoding categorical data#

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder_X=OneHotEncoder(categorical_features=[0])
X=onehotencoder_X.fit_transform(X).toarray()
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)


# splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_test, X_train, y_test, y_train=train_test_split(X,y,test_size=0.2, random_state=0)

# feature scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)






























