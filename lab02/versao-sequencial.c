/*
  * Programa: Algoritmo sequencial para multiplicacao de matrizes quadradas | Versao utilizada para calculo do ganho de desempenho
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
float *outputMatrix; // vetor de saida
int size; // dimensao das matrizes de entrada

/* Funcao para analisar a corretude da matriz de saida. 
  * Retorna 0 se existem erros ou 1 em caso de estar tudo certo
  * Como as matrizes foram inicializadas com o valor 1 e 2, a matriz de saida deve conter o elemento 1 * 2 * size em todas as posicoes
*/
int analyzeOutputCorrectness(float **output, int size) {
  float expectedValue = 2 * size;
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      if ((*output)[i*size + j] != expectedValue) {
        printf("Erro na posicao [%d][%d], valor esperado eh de %lf e o encontrado eh de %lf", i, j, expectedValue, (*output)[i*size + j]);
        return 0;
      }
    }
  }

  return 1;
}

int main(int argc, char* argv[]) {

  double start, end, delta;

  // leitura e avaliacao dos parametros de entrada (linha de comando)
  if (argc < 2) {
    printf("Comando incorreto. Digite: %s <dimensao das matrizes> \n", argv[0]);
    return 1;
  }

  GET_TIME(start);

  size = atoi(argv[1]);

  // alocacao de memoria para as estruturas de dados
  firstInputMatrix = (float *) malloc(sizeof(float) * size * size);
  if (firstInputMatrix == NULL) {
    printf("Erro de alocacao de memoria para primeira matriz de entrada");
    return 2;
  }

  secondInputMatrix = (float *) malloc(sizeof(float) * size * size);
  if (secondInputMatrix == NULL) {
    printf("Erro de alocacao de memoria para segunda matriz de entrada");
    return 2;
  }

  outputMatrix = (float *) malloc(sizeof(float) * size * size);
  if (secondInputMatrix == NULL) {
    printf("Erro de alocacao de memoria para matriz de saida");
    return 2;
  }

  // inicializacao das estruturas de dados de entrada e saida
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      firstInputMatrix[i*size + j] = 1;
      secondInputMatrix[i*size + j] = 2;
      outputMatrix[i*size + j] = 0;
    }
  }

  GET_TIME(end);
  delta = end - start;
  printf("Tempo inicializacao (a): %lf\n", delta);

  // multiplicacao da matriz pelo vetor

  GET_TIME(start);

  // Percorre as linhas da primeira matriz
  for (int line = 0; line < size; line++) {
    // Percorre as colunas da segunda matriz
    for (int column = 0; column < size; column++) {
      // Percorre a linha da primeira matriz e coluna da segunda
      for (int i = 0; i < size; i++) {
        outputMatrix[line*size + column] += firstInputMatrix[line*size + i] * secondInputMatrix[i*size + column];
      }
    }
  }

  GET_TIME(end);
  delta = end - start;
  printf("Tempo multiplicacao sequencial (b): %lf\n", delta);

  // exibicao dos resultados
  // puts("Matriz de saida: ");
  // for (int i = 0; i < size; i++) {
  //   for (int j = 0; j < size; j++) {
  //     printf("%.1lf ", outputMatrix[i*size + j]);
  //   }
  //   printf("\n");
  // }
  // puts("");

  GET_TIME(start);

  if (analyzeOutputCorrectness(&outputMatrix, size) == 1) printf("Saida correta. Todas as posicoes da matriz de saida conferem. \n");

  // liberacao da memoria
  free(firstInputMatrix);
  free(secondInputMatrix);
  free(outputMatrix);

  GET_TIME(end);
  delta = end - start;
  printf("Tempo finalizacao (c): %lf\n", delta);

  return 0;
}