import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.losses import Huber


# Path to the dataset file
dataset_path = "perf_output_all_java.csv"

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