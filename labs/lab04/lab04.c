/*
  * Programa: Algoritmo concorrente para impressao de mensagens em ordem especifica usando sincronizacao por condicao
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 2 - Laboratorio 4
  * Data: Agosto de 2021
  
  * Condicao logica da aplicacao: 
    * A thread 2 imprime sua mensagem em primeiro lugar
    * A thread 3 imprime sua mensagem em ultimo lugar 
    * A ordem em que as threads 1 e 4 imprimem suas mensagem nao importa, desde que as duas condicoes acima sejam satisfeitas
*/
#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>

// Total de Threads a serem criadas, uma por mensagem
#define NTHREADS  4

/* Variaveis globais */
int totalMessages = 0; // variavel que indica quantas mensagens ja foram impressas para evitar situacoes de deadlock
pthread_mutex_t mutex; // variavel para garantir a sincronizacao por exclusao mutua
pthread_cond_t condWelcome, condComeBack; // variaveis de controle das condicoes do problema

// Thread 1 - imprime "Fique a vontade" apenas apos a mensagem de boas vindas
void *printFeelFree (void *t) {
  pthread_mutex_lock(&mutex);
  if (totalMessages == 0) { // entra em espera se T2 ainda nao tiver imprimido
    pthread_cond_wait(&condWelcome, &mutex);
  }
  pthread_mutex_unlock(&mutex); 

  printf("Fique a vontade.\n");

  pthread_mutex_lock(&mutex);
  totalMessages++; // atualiza o total de mensagens ja impressas
  pthread_cond_signal(&condComeBack); // sinaliza pra caso T3 esteja esperando para executar
  pthread_mutex_unlock(&mutex); 

  pthread_exit(NULL);
}

// Thread 2 - imprime "Seja bem-vindo"
void *printWelcome (void *t) {
  printf("Seja bem-vindo! \n");

  pthread_mutex_lock(&mutex);
  totalMessages++; // atualiza o total de mensagens ja impressas
  pthread_cond_broadcast(&condWelcome); // sinaliza as outras threads que estejam esperando para que possam imprimir
  pthread_mutex_unlock(&mutex);

  pthread_exit(NULL);
}

// Thread 3 - imprime "Volte sempre!"
void *printComeBack (void *t) {
  pthread_mutex_lock(&mutex);
  while (totalMessages < 3) { // entra em espera se as outras threads ainda nao tiverem imprimido suas mensagens
    pthread_cond_wait(&condComeBack, &mutex);
  }
  pthread_mutex_unlock(&mutex); 

  printf("Volte sempre!\n");
  pthread_exit(NULL);
}

// Thread 4 - imprime "Sente-se por favor." 
void *printPleaseSit (void *t) {
  pthread_mutex_lock(&mutex);
  if (totalMessages == 0) { // entra em espera se T2 ainda nao tiver imprimido
    pthread_cond_wait(&condWelcome, &mutex);
  }
  pthread_mutex_unlock(&mutex); 

  printf("Sente-se por favor.\n");

  pthread_mutex_lock(&mutex);
  totalMessages++; // atualiza o total de mensagens ja impressas
  pthread_cond_signal(&condComeBack); // sinaliza pra caso T3 esteja esperando para executar
  pthread_mutex_unlock(&mutex); 

  pthread_exit(NULL);
}

// Funcao para criar as threads
void createThreads(pthread_t *tids, int numThreads) {
  int error;

  error = pthread_create(&tids[3], NULL, printFeelFree, NULL);
  error = pthread_create(&tids[2], NULL, printWelcome, NULL);
  error = pthread_create(&tids[1], NULL, printComeBack, NULL);
  error = pthread_create(&tids[0], NULL, printPleaseSit, NULL);

  if (error) {
    fprintf(stderr, "Erro na criacao das threads \n");
    exit(1);
  }
}

// Funcao para aguardar o termino das threads
void joinThreads(pthread_t *tids, int numThreads) {
  for (int i = 0; i < numThreads; i++) {
    if (pthread_join(tids[i], NULL)) {
      fprintf(stderr, "Erro no join das threads \n");
      exit(2);
    }
  }
}

// Funcao para inicializar o mutex (lock de exclusao mutua) e as variaveis de condicao
void init(pthread_mutex_t *mutex, pthread_cond_t *condWelcome, pthread_cond_t *condComeBack) {
  pthread_mutex_init(mutex, NULL);
  pthread_cond_init (condWelcome, NULL);
  pthread_cond_init (condComeBack, NULL);
}

// Funcao para desalocar variaveis
void destroy(pthread_mutex_t *mutex, pthread_cond_t *condWelcome, pthread_cond_t *condComeBack) {
  pthread_mutex_destroy(mutex);
  pthread_cond_destroy(condWelcome);
  pthread_cond_destroy(condComeBack);
}

// Funcao principal
int main(int argc, char *argv[]) {
  pthread_t tids[NTHREADS]; // identificadores das threads no sistema
  
  init(&mutex, &condWelcome, &condComeBack);
  createThreads(tids, NTHREADS);
  joinThreads(tids, NTHREADS);
  destroy(&mutex, &condWelcome, &condComeBack);

  return 0;
}