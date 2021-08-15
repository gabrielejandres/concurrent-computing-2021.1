/*
  * Programa: Algoritmo concorrente para calcular o valor de pi
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 1 - Lista  1
  * Data: Agosto de 2021
*/

#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include "timer.h"

// Variaveis globais
long int n;
int nthreads;

// Estruturas de dados
// typedef struct {
//   long int id; // identificador do elemento que a thread ira processar
//   long int n; 
//   long int nthreads; // dimensao das estruturas de entrada
// } tArgs;

// Funcao das threads
void* calculatePi(void *arg) {
  int id = (long int) arg; // identificador da thread

  double *localSum; // variavel local de soma de elementos
  int sign; // sinal de um elemento da soma

  // long int blockSize = n / nthreads; // tamanho do bloco de cada thread
  // long int start = id * blockSize; // elemento inicial do bloco da thread
  // long int end; // elemento final (nao processado) do bloco da thread

  localSum = (double *) malloc(sizeof(double));
  if (localSum == NULL) {
    fprintf(stderr, "Erro na alocacao para a soma local");
    exit(1);
  }
  *localSum = 0;

  // // se houver resto a ultima thread que vai processa-lo
  // if (id == nthreads - 1) {
  //   end = n;
  // } else {
  //   end = start + blockSize; 
  // }

  // soma os elementos do bloco da thread
  for(int i = id; i < n; i+=nthreads) {
    sign = i % 2 == 0 ? 1 : -1;
    *localSum += (sign * ((double) 1 / (2 * i + 1)));
  }

  // retorna o resultado da soma local
  pthread_exit((void *) localSum);
}

// Funcao principal
int main(int argc, char *argv[]) {
  double pi; // valor total de pi
  double piSeq; // valor total de pi sequencial
  int sign = -1; // controle do sinal na soma
  pthread_t *tid; // indentificadores das threads no sistema
  double *retorno; // valor de retorno das threads
  double start, end;

  // recebe e valida os parametros de entrada (valor de n, numero de threads)
  if (argc < 3) {
    fprintf(stderr, "Digite: %s <valor de n> <numero de threads>\n", argv[0]);
    return 1;
  }

  n = atol(argv[1]);
  nthreads = atoi(argv[2]);

  // SEQUENCIAL
  GET_TIME(start);
  for (long int i = 0; i < n; i++) {
    sign *= -1;
    piSeq += (sign * ((double) 1 / (2 * i + 1)));
  }
  piSeq = 4 * piSeq;
  GET_TIME(end);
  printf("Valor de pi sequencial: %f \n", piSeq);
  printf("Tempo sequencial: %lf\n", end - start);

  // CONCORRENTE 
  // aloca memória pros identificadores das threads
  GET_TIME(start);
  tid = (pthread_t *) malloc(sizeof(pthread_t) * nthreads);
  if (tid == NULL) {
    fprintf(stderr, "Erro na alocacao de memoria para tid \n");
    return 2;
  }

  // cria as threads
  for(long int i = 0; i < nthreads; i++) {
    if (pthread_create(tid + i, NULL, calculatePi, (void *) i)) {
      fprintf(stderr, "Erro na criacao das threads \n");
      return 3;
    }
  }

  // aguarda o termino das threads
  for(long int i = 0; i < nthreads; i++) {
    if (pthread_join(*(tid + i), (void **) &retorno)) {
      fprintf(stderr, "Erro na criacao das threads \n");
      return 3;
    }
    // soma global
    pi += *retorno;
    free(retorno);
  }

  pi = 4 * pi;
  GET_TIME(end);
  printf("Valor de pi concorrente: %f \n", pi);
  printf("Tempo concorrente: %lf\n", end - start);

  // libera as areas de memoria alocadas
  free(tid);

  return 0;
}