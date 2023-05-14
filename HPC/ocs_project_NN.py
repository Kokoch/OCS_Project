# -*- coding: utf-8 -*-

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

# Can be used to replace the dataset by arguments.
# import sys
# if sys.argv[1] != None:
#     dataset_path = str(sys.argv[1])


""" Data visualisation """

# Load dataset from file
df = pd.read_csv(dataset_path)

# Print column names and first few rows
print("Column names:")
print(df.columns)

print("\nFirst few rows:")
print(df.head())

# Load dataset from file
df = pd.read_csv(dataset_path)

# Count the number of occurrences of each type
type_counts = df['Type'].value_counts()

# Create a pie chart showing the proportion of each type
labels = ['Int', 'float', 'neg']
sizes = [type_counts[1], type_counts[2], type_counts[3]]
colors = ['lightblue', 'lightgreen', 'pink']
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Type Proportion of the Dataset')
plt.show()

# Load dataset from file
df = pd.read_csv(dataset_path)

# Count the number of occurrences of each size value
size_counts = df['Size'].value_counts()

# Create a bar chart showing the proportion of each size value
labels = size_counts.index.astype(str)
sizes = size_counts.values
colors = ['lightblue', 'lightgreen', 'pink']
plt.bar(labels, sizes, color=colors)
plt.title('Size Proportion of the Dataset')
plt.xlabel('Size')
plt.ylabel('Count')
plt.show()

# Group range values into bins
bins = pd.cut(df['Range'], bins=range(0, 1000, 100), include_lowest=True)
range_counts = bins.value_counts(sort=False)

# Create a bar chart showing the proportion of each range bin
labels = [f"<{i+99}" for i in range(0, 900, 100)]
sizes = range_counts.values
colors = ['lightblue', 'lightgreen', 'pink', 'orange', 'purple', 'gray', 'red', 'yellow', 'brown']
plt.bar(labels, sizes, color=colors)
plt.title('Range Proportion of the Dataset')
plt.xlabel('Range')
plt.ylabel('Count')
plt.show()


""" Pre-Processing """

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


""" Training """

X = df.iloc[:, :-1] # select all columns except the last one
y = df.iloc[:, -1] # select the last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss=Huber(), optimizer=Adam(learning_rate= 0.001))

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# Evaluate the model on the test data
test_loss = model.evaluate(X_test, y_test)

# Select 5 random rows from the dataset
sample_df = df.sample(n=5)
# Extract the input features from the sample dataset
X_sample = sample_df.iloc[:, :-1].values.astype('float32')
# Make predictions using the model
y_pred = model.predict(X_sample)
errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
print(f"Results for model with {10} epochs:")
for j in range(len(sample_df)):
    print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
    print("")


""" Epochs_param optimization """

# Define input and output variables for training
X = df.iloc[:, :-1] # select all columns except the last one
y = df.iloc[:, -1] # select the last column

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to train a model and return its history
def train_model(n_epochs):
    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss=Huber(), optimizer=Adam(learning_rate= 0.001))
    history = model.fit(X_train, y_train, epochs=n_epochs, batch_size=32, verbose=0)
    return history

# Train a series of models with varying numbers of epochs
n_epochs_list = [5, 10, 25, 50]
loss_list = []
for n_epochs in n_epochs_list:
    history = train_model(n_epochs)
    loss_list.append(history.history['loss'][-1])

    # Select 5 random rows from the dataset
    sample_df = df.sample(n=5)
    # Extract the input features from the sample dataset
    X_sample = sample_df.iloc[:, :-1].values.astype('float32')
    # Make predictions using the model
    y_pred = model.predict(X_sample)
    errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
    print(f"\nResults for model with {n_epochs} epochs:")
    for j in range(len(sample_df)):
        print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
        print("\n")

# Plot the loss as a function of number of epochs
plt.plot(n_epochs_list, loss_list, 'bo-')
plt.xlabel('Number of epochs')
plt.ylabel('Loss')
plt.title('Training loss as a function of number of epochs')
plt.show()


""" Batch size optimisation """

# Define input and output variables for training
X = df.iloc[:, :-1] # select all columns except the last one
y = df.iloc[:, -1] # select the last column

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to train a model and return its history
def train_model(n_batch):
    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss=Huber(), optimizer=Adam(learning_rate= 0.001))
    history = model.fit(X_train, y_train, epochs=25, batch_size=n_batch, verbose=0)
    return history

# Train a series of models with varying numbers of epochs
n_batch_list = [32, 64, 128, 256]
loss_list = []
for n_batch in n_batch_list:
    history = train_model(n_batch)
    loss_list.append(history.history['loss'][-1])

    # Select 5 random rows from the dataset
    sample_df = df.sample(n=5)
    # Extract the input features from the sample dataset
    X_sample = sample_df.iloc[:, :-1].values.astype('float32')
    # Make predictions using the model
    y_pred = model.predict(X_sample)
    errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
    print(f"\nResults for model with {n_batch} as batch size:")
    for j in range(len(sample_df)):
        print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
        print("\n")

# Plot the loss as a function of number of epochs
plt.plot(n_batch_list, loss_list, 'bo-')
plt.xlabel('batch size')
plt.ylabel('Loss')
plt.title('Training loss as a function of the batch size')
plt.show()

# Define input and output variables for training
X = df.iloc[:, :-1] # select all columns except the last one
y = df.iloc[:, -1] # select the last column

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to train a model and return its history
def train_model(n_lr):
    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss=Huber(), optimizer=Adam(learning_rate= n_lr))
    history = model.fit(X_train, y_train, epochs=25, batch_size=256, verbose=0)
    return history

# Train a series of models with varying numbers of epochs
n_lr_list = [0.0001, 0.001, 0.01, 0.1]
loss_list = []
for n_lr in n_lr_list:
    history = train_model(n_lr)
    loss_list.append(history.history['loss'][-1])

    # Select 5 random rows from the dataset
    sample_df = df.sample(n=5)
    # Extract the input features from the sample dataset
    X_sample = sample_df.iloc[:, :-1].values.astype('float32')
    # Make predictions using the model
    y_pred = model.predict(X_sample)
    errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
    print(f"\nResults for model with {n_lr} as learning rate:")
    for j in range(len(sample_df)):
        print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
        print("\n")

# Plot the loss as a function of number of epochs
plt.plot(n_lr_list, loss_list, 'bo-')
plt.xlabel('learning rate')
plt.ylabel('Loss')
plt.title('Training loss as a function of the learning rate')
plt.show()


""" FINAL MODEL """

X = df.iloc[:, :-1] # select all columns except the last one
y = df.iloc[:, -1] # select the last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss=Huber(), optimizer=Adam(learning_rate= 0.01))

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=25, batch_size=256, verbose=1)

# Select 5 random rows from the dataset
sample_df = df.sample(n=5)
# Extract the input features from the sample dataset
X_sample = sample_df.iloc[:, :-1].values.astype('float32')
# Make predictions using the model
y_pred = model.predict(X_sample)
errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
for j in range(len(sample_df)):
    print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
    print("")
