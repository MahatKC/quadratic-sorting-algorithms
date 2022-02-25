#include <stdio.h>
#include <time.h>

void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

int selectionSort(int array[], int size){
  int iter_count=0, i, j, min, aux;
  /*clock_t t0,t1;
  double time_double;
  t0 = clock();*/
  for(j=0; j<size-1; j++){
    /*if(j%1000==0){
        t1 = clock() - t0;
        time_double = ((double)t1)/(CLOCKS_PER_SEC/1000);
        printf("j: %d TIME: %lf SEC\n", j, time_double/1000.0);
        t0 = clock();
    }*/
    min = j;
    for(i=j+1; i<size; i++){
      iter_count++;
      if(array[i] < array[min]){
          min = i;
      }
    }
    if(array[min]!=array[j]){
      aux = array[min];
      array[min] = array[j];
      array[j] = aux;
    }
  }
  return iter_count;
}

int bubbleSort(int array[], int size){
  int iter_count=0, i, j, aux;

  for(j=0; j<size-1; j++){
    for(i=0; i<size-j-1; i++){
      iter_count++;
      if(array[i] > array[i+1]){
        aux = array[i];
        array[i] = array[i+1];
        array[i+1] = aux;
      }
    }
  }
  return iter_count;
}

int insertionSort(int array[], int size) {
  int iter_count=0, i, j, aux;

  for(i=1; i<size; i++){
    aux = array[i];
    j = i-1;

    while (j>=0 && array[j]>aux) {
      iter_count++;
      array[j+1] = array[j];
      j--;
    }
    array[j+1] = aux;
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