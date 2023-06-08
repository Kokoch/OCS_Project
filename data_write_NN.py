import os
import sys

# Recovering the args to include them in the dataset
epochs = int(sys.argv[1])
print("Epochs in model training:", epochs)

batch_size = int(sys.argv[2])
print("Batch Size in model training:", batch_size)

learning_rate = int(sys.argv[3])
learning_rate = str(1/learning_rate)
print("Learning Rate in model training:", learning_rate)

filenumber = str(sys.argv[4])
print("File Number:", filenumber)

NN_file = 'NNergy/outputs/NN_loss' + filenumber + '.txt'
with open(NN_file, 'r') as nf:
	loss = nf.read()

filename = 'NNergy/outputs/perf_output' + filenumber + '.txt'
with open(filename, 'a') as f:
    f.write("\nEpochs:" + str(epochs) + ":")
    f.write("\nBatch Size:" + str(batch_size) + ":")
    f.write("\nLearning Rate:" + learning_rate + ":")
    f.write("\nTotal Error Margin:" + loss + ":\n")
