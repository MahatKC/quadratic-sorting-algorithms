import time
import ctypes
import os
import pathlib
import numpy as np
np.set_printoptions(precision=6)

def selectionSortProgramiz(array, size):
    #SOURCE: https://www.programiz.com/dsa/selection-sort

    tt0 = time.time()

    for step in range(size):
        if step%1000==0:
            tt1 = time.time()
            print(f"step {step}, {tt1-tt0} sec")
            tt0 = time.time()
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

def openFile(folder, filename):
    file = open(folder+"/"+filename+".txt", "r")
    array = []
    for line in file:
        array.append(int(line))
   
    file.close()
    return array

def main():
    libname = pathlib.Path().absolute() / "sorting_algorithms.so"
    functiontest = ctypes.CDLL(libname)
    #os.nice(-19)

    sizes = [100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000, 75000, 100000, 200000, 500000]
    set_names = ["Aleatórios", "Decrescentes", "Ordenados", "ParcialmenteOrdenados"]
    set_letters = ["a", "d", "o", "po"]
    algorithms = ["b", "i", "s"]

    for set_index in range(4): 
    #itera pelos diferentes tipos de conjuntos
        set_name = set_names[set_index]
        set_letter = set_letters[set_index]
        
        for size in sizes: 
        #itera pelos diferentes tamanhos de conjuntos
            array = openFile(set_name, set_letter+str(size))
            
            for algorithm in algorithms:
            #itera pelos diferentes algoritmos

                for i in range(3):
                #executa 3 iterações para o arquivo selecionado
                    arr = (ctypes.c_int * len(array))(*array)
                    t0 = time.time()
                    if algorithm=="b":
                        iter_count = functiontest.bubbleSort(arr, size)
                    elif algorithm=="i":
                        iter_count = functiontest.insertionSort(arr, size)
                    else:
                        iter_count = functiontest.selectionSort(arr, size)
                    t1 = time.time()

                    print(f"Alg: {algorithm}| Set: {set_letter}{str(size)}| Iter {i}| Tempo: {round(t1-t0,6)}s| Count: {iter_count}")

if __name__ == "__main__":
    main()
