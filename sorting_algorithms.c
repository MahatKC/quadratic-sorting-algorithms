#include <stdio.h>
#include <time.h>

// function to swap the the position of two elements
void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

int selectionSort(int array[], int size){
    int iter_count = 0;
  /*clock_t t0,t1;
  double time_double;
  t0 = clock();*/
  for(int step=0; step<size-1; step++){
    /*if(step%1000==0){
        t1 = clock() - t0;
        time_double = ((double)t1)/(CLOCKS_PER_SEC/1000);
        printf("STEP: %d TIME: %lf SEC\n", step, time_double/1000.0);
        t0 = clock();
    }*/
    int min_idx = step;
    for(int i=step+1; i<size; i++){

      // To sort in descending order, change > to < in this line.
      // Select the minimum element in each loop.
      if(array[i] < array[min_idx]){
          iter_count++;
          min_idx = i;
      }
    }

    // put min at the correct position
    swap(&array[min_idx], &array[step]);
  }
  return iter_count;
}

int bubbleSort(int array[], int size){
    int iter_count = 0;

  // loop to access each array element
  for(int step=0; step<size-1; step++){
      
    // loop to compare array elements
    for(int i=0; i<size-step-1; i++){
      
      // compare two adjacent elements
      // change > to < to sort in descending order
      if(array[i] > array[i+1]){
          iter_count++;
        
        // swapping occurs if elements
        // are not in the intended order
        int temp = array[i];
        array[i] = array[i+1];
        array[i+1] = temp;
      }
    }
  }
  return iter_count;
}

int insertionSort(int array[], int size) {
    int iter_count = 0;

  for(int step=1; step<size; step++){
    int key = array[step];
    int j = step-1;

    // Compare key with each element on the left of it until an element smaller than
    // it is found.
    while (key<array[j] && j>=0) {
        iter_count++;
      array[j+1] = array[j];
      j--;
    }
    array[j+1] = key;
  }
  return iter_count;
}

/*
// function to print an array
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
  printf("\n");
}*/

/*
void openFile(int array[], char folder[], char filename[], int size){
    FILE *file;
    char linha[100], file_path[80];
    
    snprintf(file_path, sizeof(file_path), "%s%s%s%s", folder, "/a", filename, ".txt");

    file = fopen(file_path, "r");

    for(int i=0; i<size; i++){
        fgets(linha, 100, file);
        array[i] = atoi(linha);
    }
}*/

/*
int main(){
    int size = 2000000;
    char size_str[10];
    sprintf(size_str, "%d", size);
    int array[size];

    openFile(array, "Aleatórios", size_str, size);
    selectionSort(array, size);

    return 0;
}*/