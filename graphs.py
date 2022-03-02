import matplotlib.pyplot as plt
import pandas as pd
pd.set_option("display.precision", 8)

sizes = [100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000, 75000, 100000, 200000, 500000, 750000, 1000000, 1250000, 1500000, 2000000]
set_names = ["Aleatórios", "Decrescentes", "Ordenados", "ParcialmenteOrdenados"]
set_letters = ["a", "d", "o", "po"]
algorithms = ["b", "i", "s"]
alg_dict = {"b": "Bubble Sort", "i": "Insertion Sort", "s": "Selection Sort"}

csv_file = pd.read_csv("Resultados.csv") 
for set_name in set_names:
    set_mask = csv_file['Conjunto'] == set_name
    set_data = csv_file[set_mask]
    bubble_mask =  set_data['Algoritmo'] == 'Bubble Sort'
    bubble_data = set_data[bubble_mask]
    insertion_mask = set_data['Algoritmo'] == 'Insertion Sort'
    insertion_data = set_data[insertion_mask]
    selection_mask = set_data['Algoritmo'] == 'Selection Sort'
    selection_data = set_data[selection_mask]

    plt.figure()
    bubble_data.plot(x='Tamanho', y='Tempo')
    insertion_data.plot(x='Tamanho', y='Tempo')
    selection_data.plot(x='Tamanho', y='Tempo')
    plt.show()