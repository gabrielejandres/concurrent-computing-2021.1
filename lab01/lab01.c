/*
  * Programa: Programa concorrente para elevar elementos de um vetor ao quadrado
  * Autor: Gabriele Jandres Cavalcanti
  * Universidade Federal do Rio de Janeiro
  * Data: Julho de 2021
*/

#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>

// Tamanho do vetor de elementos
#define SIZE 10000

// Total de Threads a serem criadas
#define NTHREADS 2

// Vetores globais
int array[SIZE];
int expectedOutputArray[SIZE];

// Funcao para inicializar o array com valores de 1 a SIZE
void initializeArray() {
  for (int i = 0; i < SIZE; i++) 
    array[i] = i + 1;
}

// Funcao para preencher o array de saida esperada
void fillExpectedOutputArray() {
  for (int i = 1; i <= SIZE; i++)
    expectedOutputArray[i - 1] = i * i;
}

// Funcao que as threads irao executar para elevar os elementos do vetor ao quadrado
void* squareArrayElements(void *arg) {
  int initialIndex = *((int *) arg); // indice inicial pode ser 1 ou 2, dependendo da thread que esta executando

  // A thread 1 vai atualizar os indices impares e a thread 2 vai atualizar os indices pares do vetor
  for (int i=initialIndex; i <= SIZE; i+=2)
    array[i] *= array[i];

  pthread_exit(NULL);
}

// Funcao para comparar o array de saida esperado com a saida obtida
void analyzeOutputCorrectness() {
  // Preenche o array de saida com os valores esperados
  fillExpectedOutputArray();

  for (int i = 0; i < SIZE; i++) {
    if (array[i] != expectedOutputArray[i]) {
      printf("Erro na posicao %d, valor esperado eh de %d e o encontrado eh de %d", i, expectedOutputArray[i], array[i]);
      exit(1);
    }
  }
  printf("Saida correta. Todas as posicoes conferem. \n");
}

// Funcao para imprimir o array de saida
void printArray() {
  for (int i = 0; i < SIZE; i++)
    printf("%d \n", array[i]);
}

// Funcao principal 
int main(void) {
  int i;
  pthread_t tid[NTHREADS]; // identificador da thread no sistema
  int ident[NTHREADS]; // identificador local da thread

  // Inicializa o array com valores de 1 a SIZE
  initializeArray();

  // Cria as duas threads
  for(i=0; i < NTHREADS; i++) {
    ident[i] = i + 1;
    if (pthread_create(&tid[i], NULL, squareArrayElements, (void *)&ident[i]))
      printf("Erro ao criar a thread %d! \n", ident[i]);
  }
	
  // Espera as threads terminarem a execução
  for(i=0; i < NTHREADS; i++) {
    if (pthread_join(tid[i], NULL))
      printf("Erro com o join \n");
  }

  // Imprime o array resultante
  // printArray();
	
  // Analisa a corretude do array de saída
  analyzeOutputCorrectness();

  return 0;
}
