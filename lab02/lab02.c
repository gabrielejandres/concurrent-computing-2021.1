/*
  * Programa: Algoritmo concorrente para o problema de multiplicacao de matrizes quadradas
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 1 - Laboratorio 2
  * Data: Julho de 2021
*/

#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include "timer.h"

/* Variaveis globais */

float *firstInputMatrix; // primeira matriz de entrada
float *secondInputMatrix; // primeira matriz de entrada
float *outputMatrix; // matriz de saida
int nthreads; // numero de threads

/* Estruturas de dados */

typedef struct {
  int id; // identificador do elemento que a thread ira processar
  int size; // dimensao das matrizes de entrada
} tArgs;

/* Funcoes */

/* Funcao que as threads executarao para multiplicar as matrizes 
  * Cada thread fica responsavel por linhas intercaladas da matriz de saida 
*/
void* multiplyMatrices(void *arg) {
  tArgs *args = (tArgs*) arg;
  int initialLine = args->id; // linha inicial depende da thread que esta executando
  
  // Percorre as linhas da primeira matriz
  for (int line = initialLine;  line < args->size; line+=nthreads) {
    // Percorre as colunas da segunda matriz
    for (int column = 0; column < args->size; column++) {
      // Percorre a linha da primeira matriz e coluna da segunda
      for (int i = 0; i < args->size; i++) {
        outputMatrix[line*args->size + column] += firstInputMatrix[line*args->size + i] * secondInputMatrix[i*args->size + column];
      }
    }
  }
  pthread_exit(NULL);
}

// Funcao que aloca memoria para as matrizes de entrada e saida
void allocateMemoryToMatrices(float **firstMatrix, float **secondMatrix, float **output, int size) {
  (*firstMatrix) = (float *) malloc(sizeof(float) * size * size);
  if (firstMatrix == NULL) {
    printf("Erro de alocacao de memoria para primeira matriz de entrada");
    exit(2);
  }

  (*secondMatrix) = (float *) malloc(sizeof(float) * size * size);
  if (secondMatrix == NULL) {
    printf("Erro de alocacao de memoria para segunda matriz de entrada");
    exit(2);
  }

  (*output) = (float *) malloc(sizeof(float) * size * size);
  if (output == NULL) {
    printf("Erro de alocacao de memoria para matriz de saida");
    exit(2);
  }
}

// Funcao que aloca memoria para as matrizes de entrada e saida
void initializeMatrices(float **firstMatrix, float **secondMatrix, float **output, int size) {
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      (*firstMatrix)[i*size + j] = 1;
      (*secondMatrix)[i*size + j] = 2;
      (*output)[i*size + j] = 0;
    }
  }
}

// Funcao para criar as threads
void createThreads(tArgs **args, pthread_t **tid, int size) {
  for (int i = 0; i < nthreads; i++) {
    ((*args)+i)->id = i;
    ((*args)+i)->size = size;
    if (pthread_create((*tid)+i, NULL, multiplyMatrices, (void*) ((*args)+i))) { 
      puts("Erro na criacao das threads");
      exit(3);
    } 
  }

  // Espera pelo termino das threads
  for (int i = 0; i < nthreads; i++) {
    pthread_join(*((*tid)+i), NULL); 
  }
}

/* Funcao para analisar a corretude da matriz de saida
  * Como as matrizes foram inicializadas com o valor 1 e 2, a matriz de saida deve conter o elemento 1 * 2 * size em todas as posicoes
*/
void analyzeOutputCorrectness(float **output, int size) {
  float expectedValue = 2 * size;
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      if ((*output)[i*size + j] != expectedValue) {
        printf("Erro na posicao [%d][%d], valor esperado eh de %lf e o encontrado eh de %lf", i, j, expectedValue, (*output)[i*size + j]);
        exit(4);
      }
    }
  }

  printf("Saida correta. Todas as posicoes da matriz de saida conferem. \n");
}

// Funcao para calcular e exibir o tempo gasto em uma tarefa
void showTaskTime(double start, char taskName[]) {
  double delta, end;
  GET_TIME(end);
  delta = end - start;
  printf("Tempo de %s: %lf\n", taskName, delta);
}

// Funcao principal
int main(int argc, char* argv[]) {

  int size; // dimensao das matrizes de entrada
  pthread_t *tid; // identificadores das threads no sistema
  tArgs *args; // idetificadores locais das threads e dimensao
  double start; // variaveis de controle de tempo

  // Leitura e avaliacao dos parametros de entrada via linha de comando
  if (argc < 3) {
    printf("Digite: %s <dimensao da matriz> <numero de threads>\n", argv[0]);
    return 1;
  }

  // Inicializacao das variaveis globais
  size = atoi(argv[1]);
  nthreads = atoi(argv[2]);

  // Certificacao de que nao havera threads desnecessarias
  if (nthreads > size) {
    nthreads = size;
  }

  // Passo 1. Alocacao de memoria para as matrizes
  GET_TIME(start);
  allocateMemoryToMatrices(&firstInputMatrix, &secondInputMatrix, &outputMatrix, size);
  showTaskTime(start, "alocacao para matrizes");

  // Passo 2. Inicializacao das matrizes de entrada e saida
  GET_TIME(start);
  initializeMatrices(&firstInputMatrix, &secondInputMatrix, &outputMatrix, size);
  showTaskTime(start, "inicializacao das matrizes");

  // Passo 3. Multiplicacao das matrizes

  // 3.1. Alocacao das estruturas de dados
  GET_TIME(start);
  tid = (pthread_t*) malloc(sizeof(pthread_t)*nthreads);
  if (tid == NULL) {
    puts("Erro de alocacao de memoria para o vetor de identificadores das threads");
    return 2;
  }

  args = (tArgs*) malloc(sizeof(pthread_t)*nthreads);
  if (args == NULL) {
    puts("Erro de alocacao de memoria");
    return 2;
  }
  showTaskTime(start, "alocacao das estruturas de dados");

  // 3.2. Cria as threads, executa a multiplicacao e espera pelo termino das threads
  GET_TIME(start);
  createThreads(&args, &tid, size);
  showTaskTime(start, "multiplicacao das matrizes");

  // Passo 4. Corretude da saida
  GET_TIME(start);
  analyzeOutputCorrectness(&outputMatrix, size);
  showTaskTime(start, "testes");

  // Passo 5. Liberacao da memoria
  GET_TIME(start);
  free(firstInputMatrix);
  free(secondInputMatrix);
  free(outputMatrix);
  free(args);
  free(tid);
  showTaskTime(start, "finalizacao");

  return 0;
}