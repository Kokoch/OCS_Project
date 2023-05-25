# -*- coding: utf-8 -*-
import sys

""" Libraries """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from keras.losses import Huber

# Path to the dataset file
dataset_path = "NN_dataset.csv"

# Arguments to choose the hyperparameters from the model training.
epochs_arg = int(sys.argv[1])
batch_size_arg = int(sys.argv[2])
learning_rate_arg = int(sys.argv[3]) 
learning_ratge_arg = 1/learning_rate_arg
filenumber = int(sys.argv[4]) 

""" Pre-Processing """ # MIGHT CONSIDER TAKING THIS OUT OF THE FILE SO THAT PERF DOES NOT CONSIDER THE PREPROCESSING

# Load dataset from file
shuffled_df = pd.read_csv(dataset_path)

""" FINAL MODEL """

#Create de energy colomn (to predict)
shuffled_df['Energy'] = shuffled_df['PKG_Energy'] + shuffled_df['RAM_Energy']
shuffled_df = shuffled_df.drop(['PKG_Energy', 'RAM_Energy','File'], axis=1)

#Replace 'Python' with 0 and 'Java' with 1 in the 'Language' column
shuffled_df['Language'] = shuffled_df['Language'].replace({'python': 0, 'java': 1})

#Select columns to normalize
cols_to_normalize = ['Range', 'Cache Misses', 'Time']

#Normalize the selected columns using min-max scaling
scaler = MinMaxScaler()

shuffled_df[cols_to_normalize] = scaler.fit_transform(shuffled_df[cols_to_normalize])

X = shuffled_df.iloc[:, :-1] # select all columns except the last one
y = shuffled_df.iloc[:, -1] # select the last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss=Huber(), optimizer=Adam(learning_rate=learning_rate_arg))

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=epochs_arg, batch_size=batch_size_arg, verbose=1)

# Select 5 random rows from the dataset
sample_df = shuffled_df.sample(n=1000)

# Extract the input features from the sample dataset
X_sample = sample_df.iloc[:, :-1].values.astype('float32')

# Make predictions using the model
y_pred = model.predict(X_sample)
errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
total_error_margin = 0
for j in range(len(sample_df)):
    total_error_margin += errors[j][0]
print("Total Error Margin:", total_error_margin/1000)

with open("NNergy/outputs/NN_loss" + str(filenumber) + ".txt", "w") as f:
    f.write(str(total_error_margin/1000))
    f.close()
