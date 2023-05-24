import os
import csv
import sys

# Récupérer la liste des fichiers perf_output*.txt dans le répertoire actuel
file_list = [filename for filename in os.listdir() if filename.startswith('perf_output') and filename.endswith('.txt')]

# Initialiser une liste de dictionnaires pour stocker les résultats de tous les fichiers
all_results = []

# Parcourir chaque fichier et extraire les résultats des compteurs de performance
for filename in file_list:
    with open(filename, 'r') as f:
        lines = f.readlines()
        epochs = ''
        batch_size = ''
        learning_rate = ''
        total_error_margin = ''
        pkg_energy = ''
        ram_energy = ''
        cache_misses = ''
        duration = ''
        for line in lines:
            if 'Epochs' in line:
                epochs = line.split(":")[1] # récupère la valeur pour "Epochs"
            elif 'Batch Size' in line:
                batch_size = line.split(":")[1] # récupère la valeur pour "Batch Size"
            elif 'Learning Rate' in line:
                learning_rate = line.split(":")[1] # récupère la valeur pour "Learning Rate"
            elif 'Total Error Margin' in line:
                total_error_margin = line.split(":")[1] # récupère la valeur pour "Total Error Margin"
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

        all_results.append({'File': filename, 'Epochs': epochs, 'Batch Size': batch_size, 'Learning Rate': learning_rate, 'Total Error Margin': total_error_margin, 'PKG_Energy': pkg_energy, 'RAM_Energy': ram_energy, 'Cache Misses': cache_misses, 'Time': duration})

# Écrire les résultats dans un fichier CSV
# Add a naming for the csv

# either use 'a' or 'w' as writing mode
# If the CSV file does not exist yet, will create it and write the headers and rows in it.
csv_path = "perf_output_NN.csv"

if os.path.exists(csv_path):
    with open(csv_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['File', 'Epochs', 'Batch Size', 'Learning Rate', 'Total Error Margin', 'PKG_Energy', 'RAM_Energy', 'Cache Misses', 'Time'])
        writer.writerows(all_results)
else:
    # When the CSV file does not exist yet
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['File', 'Epochs', 'Batch Size', 'Learning Rate', 'Total Error Margin', 'PKG_Energy', 'RAM_Energy', 'Cache Misses', 'Time'])
        writer.writeheader()
        writer.writerows(all_results)