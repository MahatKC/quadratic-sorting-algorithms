import time
import ctypes
import os
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option("display.precision", 8)

def openSetFile(folder, filename):
    file = open(folder+"/"+filename+".txt", "r")
    array = []
    for line in file:
        array.append(int(line))
   
    file.close()
    return array

def main():
    libname = pathlib.Path().absolute() / "sorting_algorithms.so"
    sorting_algorithms = ctypes.CDLL(libname)
    #os.nice(-19)

    sizes = [100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000, 75000, 100000, 200000, 500000, 750000, 1000000, 1250000, 1500000, 2000000]
    set_names = ["Aleatórios", "Decrescentes", "Ordenados", "ParcialmenteOrdenados"]
    set_letters = ["a", "d", "o", "po"]
    algorithms = ["b", "i", "s"]
    alg_dict = {"b": "Bubble Sort", "i": "Insertion Sort", "s": "Selection Sort"}

    
    first = True
    iter_t0 = time.time()

    for size in sizes: 
    #itera pelos diferentes tamanhos de conjuntos
        iter_t1 = time.time()
        print(f"Iniciando tamanho {size}, {round(iter_t1-iter_t0, 6)}s")
        iter_t0 = time.time()

        for set_index in range(4): 
        #itera pelos diferentes tipos de conjuntos
            set_name = set_names[set_index]
            set_letter = set_letters[set_index]
        
            array = openSetFile(set_name, set_letter+str(size))
            
            for algorithm in algorithms:
            #itera pelos diferentes algoritmos

                avg = 0
                for i in range(3):
                #executa 3 iterações para o arquivo selecionado
                    arr = (ctypes.c_int * len(array))(*array)
                    t0 = time.time()
                    if algorithm=="b":
                        iter_count = sorting_algorithms.bubbleSort(arr, size)
                    elif algorithm=="i":
                        iter_count = sorting_algorithms.insertionSort(arr, size)
                    else:
                        iter_count = sorting_algorithms.selectionSort(arr, size)
                    t1 = time.time()
                    avg += t1-t0

                    #print(f"Alg: {algorithm}| Set: {set_letter}{str(size)}| Iter {i}| Tempo: {round(t1-t0,6)}s| Count: {iter_count}")

                avg /= 3

                results = pd.DataFrame({
                    'Algoritmo': [alg_dict[algorithm]],
                    'Conjunto': [set_name],
                    'Tamanho': [str(size)],
                    'Tempo': [str(avg)],
                    'Contagem': [str(iter_count)]
                })

                if first:
                    first = False
                    results.to_csv("Resultados.csv",index=False)
                else:
                    file_df = pd.read_csv("Resultados.csv")
                    file_df = pd.concat([file_df,results], ignore_index=True)
                    file_df.to_csv("Resultados.csv",index=False)


    """
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
    """

if __name__ == "__main__":
    main()