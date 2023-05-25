import sys
import pandas as pd
from sklearn.utils import shuffle

#Path to the dataset file java
dataset_path_java = "java/java/outputs/perf_output_all.csv"

#Path to the dataset file python
dataset_path_python = "python/outputs/perf_output_all.csv"

df1 = pd.read_csv(dataset_path_java)

#Load the second dataset
df2 = pd.read_csv(dataset_path_python)

#Concatenate the datasets vertically
merged_df = pd.concat([df1, df2], ignore_index=True)

#Shuffle the rows of the merged dataset
shuffled_df = shuffle(merged_df, random_state=42)

#Reset the index of the shuffled dataset
shuffled_df = shuffled_df.reset_index(drop=True) 

#Specify the file path and name where you want to save the CSV file
file_path = 'NN_dataset.csv'

#Save the DataFrame to a CSV file
shuffled_df.to_csv(file_path, index=False)