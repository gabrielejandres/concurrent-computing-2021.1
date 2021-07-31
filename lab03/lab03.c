/*
  * Programa: Algoritmo concorrente para o encontrar o maior e o menor elemento de um vetor
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 1 - Laboratorio 3
  * Data: Julho de 2021
*/
#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include "timer.h"

/* Variaveis globais */
long long int numElements; // numero de elementos do vetor de entrada
int nthreads; // numero de threads
float *array; // vetor de entrada

/* Estruturas de dados */
typedef struct {
  float max; // maior elemento do vetor
  float min; // menor elemento do vetor
} infoArray;

typedef struct {
  int id; // identificador da thread
  infoArray info; // struct com maior e menor elemento do vetor ate o momento de execucao da thread
} tArgs;

/* Funcoes */
// Funcao que aloca memoria para o array de entrada
void allocateMemoryToArray(float **inputArray, int numElements) {
  (*inputArray) = (float *) malloc(sizeof(float) * numElements);
  if (*inputArray == NULL) {
    fprintf(stderr, "Erro na alocacao de memoria para o vetor de entrada \n");
    exit(2);
  }
}

// Funcao que inicializa o vetor de entrada com valores aleatórios
void initializeArray(float **inputArray, int numElements) {
  // Objetiva inicializar o gerador de números aleatórios com o valor da função time(NULL)
  srand(time(NULL));

  for (long int i = 0; i < numElements; i++) {
    (*inputArray)[i] = ((float) rand()) / ((float) RAND_MAX * numElements);
  }
}

// Funcao sequencial para encontrar o menor e maior elementos do array
void findMinAndMaxElementsSeq(float **inputArray, infoArray *seqMaxMin, int numElements) {
  // printf("0: %f \n", (*inputArray)[0]);
  for (long long int i = 1; i < numElements; i++) {
    // printf("%lld: %f \n", i, (*inputArray)[i]);
    if ((*inputArray)[i] > seqMaxMin->max) {
      seqMaxMin->max = (*inputArray)[i];
    }
    if ((*inputArray)[i] < seqMaxMin->min) {
      seqMaxMin->min = (*inputArray)[i];
    }
  }
}

// Funcao que as threads irao executar para encontrar o maior e o menor elemento do array
void* findMinAndMaxElementsConc(void *arg) {
  tArgs *args = (tArgs*) arg;
  long int id = (long int) args->id; // identificador da thread
  infoArray *concMaxMin = &args->info; // maior e menor elementos ate a execucao da thread

  long int blockSize = numElements / nthreads; // tamanho do bloco de cada thread
  long int first = id * blockSize; // elemento inicial do bloco da thread
  long int end; // elemento final (nao processado) do bloco da thread

  // Se houver resto a ultima thread que vai processa-lo
  if (id == nthreads - 1) {
    end = numElements;
  } else {
    end = first + blockSize; 
  }

  // Percorre o bloco da thread para encontrar o maior e menor do bloco
  for (long int i = first; i < end; i++) {
    if (array[i] > concMaxMin->max) {
      concMaxMin->max = array[i];
    }
    if (array[i] < concMaxMin->min) {
      concMaxMin->min = array[i];
    }
  }

  // retorna as informacoes do array
  pthread_exit((void *) concMaxMin);
}

// Funcao para criar as threads
void createThreads(pthread_t **tid, infoArray concMaxMin, int numThreads) {
  tArgs *args; // identificadores locais das threads e maior e menor elemento do array ate o momento de execucao da thread

  // Aloca memoria para as estruturas de dados
  args = (tArgs*) malloc(sizeof(tArgs) * numThreads);
  if (args == NULL) {
    fprintf(stderr, "Erro na alocacao de memoria para args \n");
    exit(2);
  }

  (*tid) = (pthread_t *) malloc(sizeof(pthread_t) * numThreads);
  if (*tid == NULL) {
    fprintf(stderr, "Erro na alocacao de memoria para tid \n");
    exit(2);
  }

  // Cria as threads
  for(long int i = 0; i < numThreads; i++) {
    (args+i)->id = i;
    (args+i)->info = concMaxMin;
    if (pthread_create((*tid) + i, NULL, findMinAndMaxElementsConc, (void *) (args+i))) {
      fprintf(stderr, "Erro na criacao das threads \n");
      exit(3);
    }
  }
}

// Funcao para aguardar o termino das threads
void joinThreads(pthread_t **tid, infoArray *concMaxMin, int numThreads) {
  infoArray *infoReturn; // valor de retorno das threads

  for(long int i = 0; i < numThreads; i++) {
    if (pthread_join(*((*tid) + i), (void **) &infoReturn)) {
      fprintf(stderr, "Erro no join das threads \n");
      exit(4);
    }

    // Atualizando os valores de maximo e minimo da main
    if (infoReturn->max > concMaxMin->max) {
      concMaxMin->max = infoReturn->max;
    }

    if (infoReturn->min < concMaxMin->min) {
      concMaxMin->min = infoReturn->min;
    }
  }
}

// Funcao que checa a corretude da solucao concorrente
void analyzeOutputCorrectness(infoArray *seqMaxMin, infoArray *concMaxMin) {
  if (seqMaxMin->max == concMaxMin->max && seqMaxMin->min == concMaxMin->min) {
    printf("Todos os dados conferem. \nMaior elemento: %.15lf | Menor elemento: %.15lf \n", concMaxMin->max, concMaxMin->min);
  } else {
    printf("Os valores de maximo e minimo divergiram! \n");
    printf("-- SEQUENCIAL -- \nMaior elemento: %.15lf | Menor elemento: %.15lf \n", seqMaxMin->max, seqMaxMin->min);
    printf("-- CONCORRENTE -- \nMaior elemento: %.15lf | Menor elemento: %.15lf \n", concMaxMin->max, concMaxMin->min);
  }
}

// Funcao principal
int main(int argc, char *argv[]) {
  infoArray seqMaxMin, concMaxMin; // variaveis para armazenar o maior e o menor elemento do array
  double start, end; // variaveis de controle de tempo
  pthread_t *tid; // identificadores das threads no sistema

  // Recebe e valida os parametros de entrada
  if (argc < 3) {
    fprintf(stderr, "Comando incorreto. Digite: %s <numero de elementos do vetor> <numero de threads>\n", argv[0]);
    return 1;
  }

  // Conversao dos parametros de entrada
  numElements = atoll(argv[1]);
  nthreads = atoi(argv[2]);

  // Aloca memoria e inicializa o vetor de entrada
  allocateMemoryToArray(&array, numElements);
  initializeArray(&array, numElements);

  // Inicializando os valores de maximo e minimo com o primeiro elemento do array
  concMaxMin.max = seqMaxMin.max = array[0];
  concMaxMin.min = seqMaxMin.min = array[0];

  // SEQUENCIAL: Encontra o maior e o menor elemento do vetor
  GET_TIME(start);
  findMinAndMaxElementsSeq(&array, &seqMaxMin, numElements);
  GET_TIME(end);
  printf("Tempo sequencial: %lf\n", end - start);

  // CONCORRENTE: Encontra o maior e o menor elemento do vetor
  GET_TIME(start);
  createThreads(&tid, concMaxMin, nthreads);
  joinThreads(&tid, &concMaxMin, nthreads);
  GET_TIME(end);
  printf("Tempo concorrente: %lf\n", end - start);

  // Checa a corretude da solução
  analyzeOutputCorrectness(&seqMaxMin, &concMaxMin);

  // Libera as areas de memoria alocadas
  free(array);
  free(tid);

  return 0;
}