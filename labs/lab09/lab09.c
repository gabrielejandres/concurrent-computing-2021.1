/*
  * Programa: Variacao da implementacao do problema produtor/consumidor onde o consumidor consome o buffer inteiro a cada execucao
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 3 - Laboratorio 9
  * Data: Outubro de 2021
*/
#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5 // tamanho do buffer

/* Variaveis globais */
sem_t fullBuffer, emptySlot; // condicao
sem_t mutexProd; // exclusao mutua entre produtores
int buffer[N]; // area de memoria compartilhada

/* Funcoes */

// Inicializa o buffer
void initializeBuffer(int n) {
  for (int i = 0; i < n; i ++)
    buffer[i] = 0;
}

// Imprime o buffer
void printBuffer(int n) {
  for (int i = 0; i < n; i ++)
    printf("%d ", buffer[i]);
  printf("\n");
}

// Funcao auxiliar para os produtores inserem dados no buffer
void insertInBuffer(int item, int id) {
  static int in = 0;
  sem_wait(&emptySlot); // aguarda slot vazio
  sem_wait(&mutexProd); // exclusao mutua entre produtores
  buffer[in] = item;
  printf("# Elemento %d inserido \n", item);
  printf("checker.insertInBuffer(%d, %d)\n", id, item);

  // sinaliza que o buffer está cheio quando o último elemento foi inserido
  if (in == (N - 1)) {
    printf("# Produtora %d sinalizou que o buffer esta cheio \n", id);
    printf("checker.sinalizeFullBuffer(%d)\n", id);
    sem_post(&fullBuffer);
  }

  in = (in + 1) % N;
  sem_post(&mutexProd);
}

// Funcao auxiliar para os consumidores removerem dados do buffer
void removeFromBuffer(int id) {
  int item;
  sem_wait(&fullBuffer); // aguarda buffer cheio
  printf("# Consumidora %d vai consumir o buffer \n", id);
  printf("checker.readBuffer(%d)\n", id);
  for(int i = 0; i < N; i++) {
    item = buffer[i];
    printf("# Elemento %d retirado \n", item);
    sem_post(&emptySlot); // sinaliza um slot vazio para cada posicao do buffer que consome
  }
}

// Thread produtora
void* producer(void * arg) {
  int *id = (int *) arg;
  while(1) {
    insertInBuffer(rand() % 5 + *id, *id);
    sleep(1);
  }
  free(arg);
  pthread_exit(NULL);
}

// Thread consumidora
void* consumer(void * arg) {
  int *id = (int *) arg;
  while(1) {
    removeFromBuffer(*id);
    sleep(1);
  }
  free(arg);
  pthread_exit(NULL);
}

// Funcao para criar as threads
void createThreads(pthread_t *tids, int numProducers, int numConsumers) {
  int *id[numProducers + numConsumers];

  // aloca espaco para os IDs das threads
  for (int i = 0; i < numProducers + numConsumers; i++) {
    id[i] = malloc(sizeof(int));
    if(id[i] == NULL) exit(-1);
    *id[i] = i + 1;
  }

  // cria as threads produtoras
  for (int i = 0; i < numProducers; i++) {
    if (pthread_create(tids + i, NULL, producer, (void *) id[i])) exit(-1); 
  }

  // cria as threads produtoras
  for (int i = 0; i < numConsumers; i++) {
    if (pthread_create(tids + i + numProducers, NULL, consumer, (void *) id[i + numProducers])) exit(-1); 
  }
}

// Funcao para aguardar o termino das threads
void joinThreads(pthread_t *tids, int numThreads) {
  for (int i = 0; i < numThreads; i++) {
    if (pthread_join(*(tids + i), NULL)) {
      fprintf(stderr, "Erro no join das threads \n");
      exit(2);
    }
  }
}

// Funcao para inicializar recursos
void init(sem_t *mutexProd, sem_t *fullBuffer, sem_t *emptySlot, pthread_t **tids, int numThreads) {
  sem_init(mutexProd, 0, 1);
  sem_init(fullBuffer, 0, 0);
  sem_init(emptySlot, 0, N);

  (*tids) = (pthread_t *) malloc(sizeof(pthread_t) * numThreads);
  if ((*tids) == NULL) {
    printf("Erro na alocacao de memoria para tids \n");
    exit(2);
  }
}

// Funcao para desalocar e finalizar recursos
void destroy(sem_t *mutexProd, sem_t *fullBuffer, sem_t *emptySlot, pthread_t *tids) {
  sem_destroy(mutexProd);
	sem_destroy(fullBuffer);
	sem_destroy(emptySlot);
  free(tids);
}

// Funcao principal
int main(int argc, char *argv[]) {
  int numProducers, numConsumers; // numero de threads produtoras e consumidoras
  pthread_t *tids; // identificadores das threads no sistema

  if (argc < 3) {
		printf("Digite %s <quantidade-de-produtores> <quantidade-de-consumidores> \n", argv[0]);
		return 1;
	}

  numProducers = atoi(argv[1]);
	numConsumers = atoi(argv[2]);

  printf("import checkProdCons\n");
  printf("checker = checkProdCons.PRODCONS()\n");

  srand(time(NULL));
  initializeBuffer(N);
  init(&mutexProd, &fullBuffer, &emptySlot, &tids, numProducers + numConsumers);
  createThreads(tids, numProducers, numConsumers);
  joinThreads(tids, numProducers + numConsumers);
  destroy(&mutexProd, &fullBuffer, &emptySlot, tids);

  return 0;
}