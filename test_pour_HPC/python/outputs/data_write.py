import os
import sys

# Recovering the args to include them in the dataset
m_size = int(sys.argv[1])
m_range = int(sys.argv[2])

m_type = str(sys.argv[3])

language = str(sys.argv[4])



#Add selection of size between 1 and 4:
if m_size == 1:
    size = 10
elif m_size == 2:
    size = 100
elif m_size == 3:
    size = 1000
elif m_size == 4:
    size = 10000    


# Positive integers (N)
if  m_type == 1 or m_type == "1":
    m_type = "int"

# Negative integers (Z)
if m_type == 2 or m_type == "2":
    m_type = "neg"
# Floats (R)
if m_type == "float" or m_type == 3 or m_type == "3":
    m_type = "float"





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