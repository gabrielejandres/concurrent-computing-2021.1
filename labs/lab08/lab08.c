/*
  * Programa: Algoritmo concorrente para impressao de mensagens em ordem especifica usando semaforos para sincronizacao condicional e exclusao mutua
  * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
  * Disciplina: Computacao Concorrente - 2021.1
  * Modulo 3 - Laboratorio 8
  * Data: Setembro de 2021
  
  * Condicao logica da aplicacao: 
    * A thread 2 imprime sua mensagem em primeiro lugar
    * A thread 3 imprime sua mensagem em ultimo lugar 
    * A ordem em que as threads 1 e 4 imprimem suas mensagem nao importa, desde que as duas condicoes acima sejam satisfeitas
*/
#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include <semaphore.h>

// Total de Threads a serem criadas, uma por mensagem
#define NTHREADS  4

/* Variaveis globais */
sem_t condWelcome, condComeBack; //semaforos para sincronizar a ordem de execucao das threads

// Thread 1 - imprime "Fique a vontade" apenas apos a mensagem de boas vindas
void *printFeelFree (void *t) {
  sem_wait(&condWelcome); // espera T2 executar 
  printf("Fique a vontade. \n");
  sem_post(&condComeBack); // incrementa o semaforo em 1 para permitir que T3 execute
  pthread_exit(NULL);
}

// Thread 2 - imprime "Seja bem-vindo"
void *printWelcome (void *t) {
  printf("Seja bem-vindo! \n");
  // Incrementa o semaforo em 2 para permitir que T1 e T4 executem (sinaliza para que as duas threads sejam desbloqueadas, se necessario)
  sem_post(&condWelcome); 
  sem_post(&condWelcome);
  pthread_exit(NULL);
}

// Thread 3 - imprime "Volte sempre!" 
void *printComeBack (void *t) {
  // Espera T1 e T4 executarem (so exibe sua mensagem apos duas sinalizacoes)
  sem_wait(&condComeBack); 
  sem_wait(&condComeBack); 
  printf("Volte sempre! \n");
  pthread_exit(NULL);
}

// Thread 4 - imprime "Sente-se por favor." apenas apos a mensagem de boas vindas
void *printPleaseSit (void *t) {
  sem_wait(&condWelcome); // espera T2 executar 
  printf("Sente-se por favor. \n");
  sem_post(&condComeBack); // incrementa o semaforo em 1 para permitir que T3 execute
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

// Funcao para inicializar os semaforos
void init(sem_t *condWelcome, sem_t *condComeBack) {
  sem_init(condWelcome, 0, 0);
  sem_init(condComeBack, 0, 0);
}

// Funcao para desalocar e finalizar os semaforos
void destroy(sem_t *condWelcome, sem_t *condComeBack) {
  sem_destroy(condWelcome);
	sem_destroy(condComeBack);
}

// Funcao principal
int main(int argc, char *argv[]) {
  pthread_t tids[NTHREADS]; // identificadores das threads no sistema

  init(&condWelcome, &condComeBack);
  createThreads(tids, NTHREADS);
  joinThreads(tids, NTHREADS);
  destroy(&condWelcome, &condComeBack);

  return 0;
}