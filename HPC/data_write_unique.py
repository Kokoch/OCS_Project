import os
import sys

# Recovering the args to include them in the dataset
m_size = int(sys.argv[1])
print("Size of the matrix to be generated:", m_size)

m_range = int(sys.argv[2])
print("Range of the matrix to be generated:", m_range)

m_type = str(sys.argv[3])
print("Type of the values contained in the matrix to be generated:", m_type)

language = str(sys.argv[4])
print("Language Used:", language)

filenumber = str(sys.argv[5])
print("File Number:", filenumber)

filename = 'python/outputs/perf_output' + filenumber + '.txt'
with open(filename, 'a') as f:
    f.write("\nSize:" + str(m_size) + ":")
    f.write("\nRange:" + str(m_range) + ":")
    f.write("\nType:" + m_type + ":")
    f.write("\nLanguage:" + language + ":")