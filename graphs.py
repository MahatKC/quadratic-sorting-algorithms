from matplotlib import lines
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
pd.set_option("display.precision", 8)

sizes = [100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000, 75000, 100000, 200000, 500000, 750000, 1000000, 1250000]
#sizes = [100, 200, 500, 1000, 2000, 5000, 7500]
set_names = ["Aleatórios", "Decrescentes", "Ordenados", "ParcialmenteOrdenados"]
set_letters = ["a", "d", "o", "po"]
algorithms = ["b", "i", "s"]
alg_dict = {"b": "Bubble Sort", "i": "Insertion Sort", "s": "Selection Sort"}

dic = {}
dic['b'] = []
dic['i'] = []
dic['s'] = []

csv_file = pd.read_csv("Resultados.csv") 
for set_name in set_names:
    set_mask = csv_file['Conjunto'] == set_name
    set_data = csv_file[set_mask]

    bubble_mask =  set_data['Algoritmo'] == 'Bubble Sort'
    bubble_data = set_data[bubble_mask]
    resultados_bubble = bubble_data['Tempo'].tolist()
    dic['b'].append(resultados_bubble)

    insertion_mask = set_data['Algoritmo'] == 'Insertion Sort'
    insertion_data = set_data[insertion_mask]
    resultados_insertion = insertion_data['Tempo'].tolist()
    dic['i'].append(resultados_insertion)

    selection_mask = set_data['Algoritmo'] == 'Selection Sort'
    selection_data = set_data[selection_mask]
    resultados_selection = selection_data['Tempo'].tolist()
    dic['s'].append(resultados_selection)

    #print(resultados_bubble)
    print(len(sizes), len(resultados_bubble), len(resultados_insertion), len(resultados_selection))
    df = pd.DataFrame({
        'tam': sizes,
        'te_bub': resultados_bubble,
        'te_ins': resultados_insertion,
        'te_sel': resultados_selection
        })

    #df = pd.DataFrame([resultados_bubble[0],resultados_bubble[1],resultados_insertion[0],resultados_insertion[1],resultados_selection[0],resultados_selection[1]])
    #df.rename(columns={0:'bubble_tamanho', 1:'bubble_tempo', 2:'insertion_tamanho', 3:'insertion_tempo', 4:'selection_tamanho', 5:'selection_tempo'},inplace=True)

    #print(np.shape(df), type(df), df, sep='\n')
    plt.figure()
    if (set_name == 'ParcialmenteOrdenados'): set_name = 'Parcialmente Ordenados'
    plt.title(set_name)
    plt.xlabel("Tamanho")
    plt.ylabel("Tempo (s)")
    plt.plot(df['tam'], df['te_bub'], color='g', label='bubble')
    plt.plot(df['tam'], df['te_ins'], color='r', label='insertion')
    plt.plot(df['tam'], df['te_sel'], color='b', label='selection')
    #set_data.plot(x='Tamanho', y='Tempo')
    #bubble_data.plot(x='Tamanho', y='Tempo')
    #insertion_data.plot(x='Tamanho', y='Tempo')
    #selection_data.plot(x='Tamanho', y='Tempo')
    plt.legend()
    plt.show()

for alg in algorithms:

    #print(len(sizes), len(resultados_bubble), len(resultados_insertion), len(resultados_selection))
    df = pd.DataFrame({
        'tam': sizes,
        'Aleatórios': dic[alg][0],
        'Decrescentes': dic[alg][1],
        'Ordenados': dic[alg][2],
        'ParcialmenteOrdenados': dic[alg][3]
        })

    plt.figure()
    plt.title(alg_dict[alg])
    plt.plot(df['tam'], df['Aleatórios'], color='g', label='Aleatórios')
    plt.plot(df['tam'], df['Decrescentes'], color='r', label='Decrescentes')
    plt.plot(df['tam'], df['Ordenados'], color='b', label='Ordenados')
    plt.plot(df['tam'], df['ParcialmenteOrdenados'], color='m', label='Parcialmente Ordenados')    
    plt.legend()
    plt.show()
