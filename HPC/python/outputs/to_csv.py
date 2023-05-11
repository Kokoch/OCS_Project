import os
import csv
import sys

# Add args in order to name the csv. If find how to append not necessary
type= list(sys.argv[1])
size= list(sys.argv[2])

# Récupérer la liste des fichiers perf_output*.txt dans le répertoire actuel
file_list = [filename for filename in os.listdir() if filename.startswith('perf_output') and filename.endswith('.txt')]

# Initialiser une liste de dictionnaires pour stocker les résultats de tous les fichiers
all_results = []

# Parcourir chaque fichier et extraire les résultats des compteurs de performance
for filename in file_list:
    with open(filename, 'r') as f:
        lines = f.readlines()
        m_size = ''
        m_range = ''
        m_type = ''
        language = ''
        pkg_energy = ''
        ram_energy = ''
        cache_misses = ''
        duration = ''
        for line in lines:
            if 'Size' in line:
                m_size = line.split(":")[1] # récupère la valeur pour "Size"
            elif 'Range' in line:
                m_range = line.split(":")[1] # récupère la valeur pour "Range"
            elif 'Type' in line:
                m_type = line.split(":")[1] # récupère la valeur pour "Type"
            elif 'Language' in line:
                language = line.split(":")[1] # récupère la valeur pour "Language"
            elif 'power/energy-pkg/' in line:
                pkg_energy = line.split()[0].replace(',', '.') # récupère la valeur pour "power/energy-pkg/"
            elif 'power/energy-ram/' in line:
                ram_energy = line.split()[0].replace(',', '.') # récupère la valeur pour "power/energy-ram/"            
            elif 'cpu/cache-misses/' in line:
                cache_misses = line.split()[0] # récupère la valeur pour "cpu/cache-misses/"
            elif 'seconds' in line:
                duration = line.split(" seconds")[0].replace(',', '.')  # récupère la valeur pour la durée
                duration = ("").join(duration)
                duration = duration.split(" ")[-1]

        all_results.append({'File': filename, 'Language': language, 'Size': m_size, 'Range': m_range, 'Type': m_type, 'PKG_Energy': pkg_energy, 'RAM_Energy': ram_energy, 'Cache Misses': cache_misses, 'Time': duration})

# Écrire les résultats dans un fichier CSV
# Add a naming for the csv

# either use 'a' or 'w' as writing mode
# If the CSV file does not exist yet, will create it and write the headers and rows in it.
csv_path = "perf_output_all.csv"

if os.path.exists(csv_path):
    print("here")
    with open(csv_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['File', 'Language', 'Size', 'Range', 'Type', 'PKG_Energy', 'RAM_Energy', 'Cache Misses', 'Time'])
        writer.writerows(all_results)
else:
    # When the CSV file does not exist yet
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['File', 'Language', 'Size', 'Range', 'Type', 'PKG_Energy', 'RAM_Energy', 'Cache Misses', 'Time'])
        writer.writeheader()
        writer.writerows(all_results)