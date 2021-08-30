/*
  * Programa: Algoritmo concorrente para somar elementos de um vetor de inteiros e atualizar valores do vetor usando sincronizacao coletiva
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 2 - Laboratorio 5
  * Data: Agosto de 2021
*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Variaveis globais */
int blockedThreads = 0; // numero de threads bloqueadas
int size; // numero de threads a serem criadas, que sera tambem o tamanho do array e o numero de iteracoes
int *array; // vetor de inteiros
pthread_mutex_t mutex; // variavel para garantir a sincronizacao por exclusao mutua
pthread_cond_t condition; // variavel de controle da condicao do problema

/* Funcoes */
// Funcao que aloca memoria para o array de entrada
void allocateMemoryToArray(int **inputArray, int numElements) {
  (*inputArray) = (int *) malloc(sizeof(int) * numElements);
  if (*inputArray == NULL) {
    printf("Erro na alocacao de memoria para o vetor \n");
    exit(2);
  }
}

// Funcao que inicializa o vetor de entrada com valores aleatórios
void initializeArray(int **inputArray, int numElements) {
  for (int i = 0; i < numElements; i++) {
    (*inputArray)[i] = rand() % 10;
  }
}

//funcao barreira
void barrier(int nthreads, int threadId, int barrierId) {
    pthread_mutex_lock(&mutex);
    // Quando a ultima thread chegar na barreira ela pode sinalizar que as outras que estao aguardando podem prosseguir
    if (blockedThreads == (nthreads - 1)) { 
      printf("Thread %d liberando execucao das threads...\n", threadId);
      char* message = barrierId == 0 ? "Fim da soma dos elementos\n\n" : "Fim da atualizacao dos elementos\n\n";
      printf("%s", message);
      pthread_cond_broadcast(&condition);
      blockedThreads = 0;
    } else {
      blockedThreads++;
      // Se nao for a ultima thread a chegar fico aguardando
      printf("Thread %d ficou bloqueada na barreira...\n", threadId);
      pthread_cond_wait(&condition, &mutex);
    }
    pthread_mutex_unlock(&mutex);
}

//funcao das threads
void *sumAndUpdateArrayElements(void *arg) {
  long int id = (long int) arg; // identificador da thread
  int *localSum; // variavel local de soma de elementos

  // Objetiva inicializar o gerador de números aleatórios com o valor da função time(NULL)
  srand(time(NULL));

  localSum = (int *) malloc(sizeof(int));
  if (localSum == NULL) {
    fprintf(stderr, "Erro na alocacao para a soma local");
    exit(3);
  }
  *localSum = 0;

  for (int i = 0; i < size; i++) {
    printf("Iteracao %d: \nThread %ld comecou a executar... \n", i, id);

    // soma os elementos do vetor
    for(int j = 0; j < size; j++) {
      // printf("array[%d] = %d\n", j, array[j]);
      *localSum += array[j];
    }

    // Primeira barreira para aguardar todas as threads somarem os elementos do vetor
    barrier(size, id, 0);

    array[id] = rand() % 10;

    // Segunda barreira para aguardar todas as threads atualizarem o elemento do vetor cujo indice eh seu id
    barrier(size, id, 1);
  }

  pthread_exit((void *) localSum);
}

// Funcao para inicializar o mutex (lock de exclusao mutua), a variavel de condicao e a estrutura de ids das threads
void init(pthread_mutex_t *mutex, pthread_cond_t *condition, pthread_t **tids, int size) {
  pthread_mutex_init(mutex, NULL);
  pthread_cond_init (condition, NULL);

  (*tids) = (pthread_t *) malloc(sizeof(pthread_t) * size);
  if ((*tids) == NULL) {
    printf("Erro na alocacao de memoria para tid \n");
    exit(2);
  }
}

// Funcao para checar a corretude do resultado
void checkOutputCorrectness(int *sumElementsOfArray) {
  int reference = sumElementsOfArray[0];

  printf("-- Valores de soma recebidos das threads --\n");
  for(int i = 0; i < size; i++) {
    printf("Thread %d: %d \n", i, sumElementsOfArray[i]);
    if (sumElementsOfArray[i] != reference) {
      printf("\nOs valores das somas calculadas pelas threads %d e %d divergem!\n", i, 0);
      exit(4);
    }
  }
  printf("\nTodas as threads calcularam o mesmo valor de soma!\n");
}

// Funcao para criar as threads
void createThreads(pthread_t *tids, int numThreads) {
  for(long int i = 0; i < size; i++) {
    if (pthread_create(tids + i, NULL, sumAndUpdateArrayElements, (void *) i)) {
      printf("Erro na criacao das threads \n");
      exit(5);
    }
  }
}

// Funcao para aguardar o termino das threads
void joinThreads(pthread_t *tids, int numThreads, int **sumElementsOfArray) {
  int *threadReturn; // valor de retorno das threads

  for (int i = 0; i < size; i++) {
    if (pthread_join(*(tids + i), (void **) &threadReturn)) {
      printf("Erro no join das threads \n");
      exit(6);
    }
    (*sumElementsOfArray)[i] = *threadReturn;
  }

  free(threadReturn);
}

// Funcao para desalocar variaveis
void destroy(pthread_mutex_t *mutex, pthread_cond_t *condition) {
  pthread_mutex_destroy(mutex);
  pthread_cond_destroy(condition);
}

// Funcao principal
int main(int argc, char *argv[]) {
  pthread_t *tids; // identificadores das threads no sistema
  int *sumElementsOfArray; // array com os valores da soma retornados pelas threads

  // Recebe e valida os parametros de entrada
  if (argc < 2) {
    printf("Comando incorreto. Digite: %s <numero de threads> \n", argv[0]);
    return 1;
  }
  size = atoi(argv[1]);

  // Alocacao para o array de somas
  allocateMemoryToArray(&sumElementsOfArray, size);

  // Alocacao e inicializacao do array de inteiros
  srand(time(NULL));
  allocateMemoryToArray(&array, size);
  initializeArray(&array, size);

  // Fluxo principal para execucao das threads
  init(&mutex, &condition, &tids, size);
  createThreads(tids, size);
  joinThreads(tids, size, &sumElementsOfArray);
  checkOutputCorrectness(sumElementsOfArray);
  destroy(&mutex, &condition);

  free(array);
  free(sumElementsOfArray);
  free(tids);

  return 0;
}