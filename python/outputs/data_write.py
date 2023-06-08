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

# Récupérer la liste des fichiers perf_output*.txt dans le répertoire actuel
file_list = [filename for filename in os.listdir() if filename.startswith('perf_output') and filename.endswith('.txt')]

# Initialiser une liste de dictionnaires pour stocker les résultats de tous les fichiers
all_results = []

# Parcourir chaque fichier et extraire les résultats des compteurs de performance
for filename in file_list:
    with open(filename, 'a') as f:
        f.write("\nSize:" + str(m_size) + ":")
        f.write("\nRange:" + str(m_range) + ":")
        f.write("\nType:" + m_type + ":")
        f.write("\nLanguage:" + language + ":")