
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.losses import Huber
from sklearn.utils import shuffle

# Path to the dataset file java
dataset_path_java = "perf_output_all_java.csv"
# Path to the dataset file python
dataset_path_python = "perf_output_all_python.csv"

# Load the first dataset
df1 = pd.read_csv(dataset_path_java)

# Load the second dataset
df2 = pd.read_csv(dataset_path_python)

# Concatenate the datasets vertically
merged_df = pd.concat([df1, df2], ignore_index=True)

# Shuffle the rows of the merged dataset
shuffled_df = shuffle(merged_df, random_state=42)

# Reset the index of the shuffled dataset
shuffled_df = shuffled_df.reset_index(drop=True)

print(shuffled_df.head())

# Create de energy colomn (to predict)
shuffled_df['Energy'] = shuffled_df['PKG_Energy'] + shuffled_df['RAM_Energy']
shuffled_df = shuffled_df.drop(['PKG_Energy', 'RAM_Energy','File'], axis=1)

# Replace 'Python' with 0 and 'Java' with 1 in the 'Language' column
shuffled_df['Language'] = shuffled_df['Language'].replace({'python': 0, 'java': 1})

# Select columns to normalize
cols_to_normalize = ['Range', 'Cache Misses', 'Time']

# Normalize the selected columns using min-max scaling
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
model.compile(loss=Huber(), optimizer=Adam(learning_rate= 0.001))

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=50, batch_size=128, verbose=1)

# Select 5 random rows from the dataset
sample_df = shuffled_df.sample(n=5)
# Extract the input features from the sample dataset
X_sample = sample_df.iloc[:, :-1].values.astype('float32')
# Make predictions using the model
y_pred = model.predict(X_sample)
errors = np.abs(y_pred - sample_df.iloc[:, -1].values.reshape(-1,1))
for j in range(len(sample_df)):
    print(f"Sample {j+1}: Predicted Energy = {y_pred[j][0]:.2f}, Actual Energy = {sample_df.iloc[j,-1]:.2f}, Error = {errors[j][0]:.2f}")
    print("")