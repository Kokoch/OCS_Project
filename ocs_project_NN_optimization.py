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
dataset_path = "python/outputs/perf_output_all.csv"

# Arguments to choose the hyperparameters from the model training.
epochs_arg = int(sys.argv[1])
batch_size_arg = int(sys.argv[2])
learning_rate_arg = int(sys.argv[3]) 
learning_ratge_arg = 1/learning_rate_arg
filenumber = int(sys.argv[4]) 

""" Pre-Processing """ # MIGHT CONSIDER TAKING THIS OUT OF THE FILE SO THAT PERF DOES NOT CONSIDER THE PREPROCESSING

# Load dataset from file
df = pd.read_csv(dataset_path)

# Create de energy colomn (to predict)
df['Energy'] = df['PKG_Energy'] + df['RAM_Energy']
df = df.drop(['PKG_Energy', 'RAM_Energy','File','Language'], axis=1)

print(df.columns)

# Select columns to normalize
cols_to_normalize = ['Range', 'Cache Misses', 'Time']

# Normalize the selected columns using min-max scaling
scaler = MinMaxScaler()

df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

# View the updated dataset with the normalized columns
print(df.head())

""" FINAL MODEL """

X = df.iloc[:, :-1] # select all columns except the last one
y = df.iloc[:, -1] # select the last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss=Huber(), optimizer=Adam(learning_rate=learning_rate_arg))

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=epochs_arg, batch_size=batch_size_arg, verbose=1)

# Evaluate the model on the test data
test_loss = model.evaluate(X_test, y_test)

# Select 5 random rows from the dataset
sample_df = df.sample(n=5)

# Extract the input features from the sample dataset
X_sample = sample_df.iloc[:, :-1].values.astype('float32')

# Make predictions using the model
y_pred = model.predict(X_sample)
errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
total_error_margin = 0
for j in range(len(sample_df)):
    print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
    print("")
    total_error_margin += errors[j][0]

with open("NNergy/outputs/NN_loss" + str(filenumber) + ".txt", "w") as f:
    #f.write(str(test_loss))
    f.write(str(total_error_margin))
    f.close()
