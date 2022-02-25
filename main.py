import time
import ctypes
import os
import pathlib
import matplotlib

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
    os.nice(-19)

    sizes = [100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000, 75000, 100000, 200000, 500000]
    set_names = ["Aleatórios", "Decrescentes", "Ordenados", "ParcialmenteOrdenados"]
    set_letters = ["a", "d", "o", "po"]
    algorithms = ["b", "i", "s"]

    for set_index in range(4): 
    #itera pelos diferentes tipos de conjuntos
        set_name = set_names[set_index]
        set_letter = set_letters[set_index]
        
        for size in size[:5]: 
        #itera pelos diferentes tamanhos de conjuntos
            array = openSetFile(set_name, set_letter+str(size))
            
            for algorithm in algorithms:
            #itera pelos diferentes algoritmos

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

                    print(f"Alg: {algorithm}| Set: {set_letter}{str(size)}| Iter {i}| Tempo: {round(t1-t0,6)}s| Count: {iter_count}")

if __name__ == "__main__":
    main()