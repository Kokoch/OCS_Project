import os
import sys

# Recovering the args to include them in the dataset
m_size = int(sys.argv[1])

m_range = int(sys.argv[2])

m_type = str(sys.argv[3])

language = str(sys.argv[4])

filenumber = str(sys.argv[5])

filename = 'python/outputs/perf_output' + filenumber + '.txt'
with open(filename, 'a') as f:
    f.write("\nSize:" + str(m_size) + ":")
    f.write("\nRange:" + str(m_range) + ":")
    f.write("\nType:" + m_type + ":")
    f.write("\nLanguage:" + language + ":")