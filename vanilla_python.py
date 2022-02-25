import time
import os

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
    #os.nice(-19)

    size = 2000000
    array = openFile("Aleatórios", "a"+str(size))
    t0 = time.time()
    selectionSortProgramiz(array, size)
    t1 = time.time()
    print(f"tempo programiz: {t1-t0} segundos")

if __name__ == "__main__":
    main()
