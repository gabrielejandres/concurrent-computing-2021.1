#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define L 4 //numero de threads leitoras
#define E 4 //numero de threads escritoras

/* Variaveis globais */

int leitores = 0; // contador de threads lendo
int escritores = 0; // contador de threads escritoras aguardando
sem_t escrita; // exclusao mutua para escritores
sem_t mutexL; // exclusao mutua entre leitores para acesso a variavel global leitores
sem_t mutexE; // exclusao mutua para acesso a variavel global escritores
sem_t fila; // fila de leitura

/* Funcoes */

// Funcao dos leitores
void *leitor(void * arg) {
  int *id = (int *) arg;
  while(1) {
    printf("Thread leitora %d tentando executar...\n", *id);
    sem_wait(&fila); // entra em espera para executar se tiver escritor aguardando

    sem_wait(&mutexL); // exclusao mutua para acesso a variavel leitores
    leitores++; // incrementa o numero de threads leitoras executando
    if (leitores == 1) { // primeiro leitor verifica se nao ha alguem escrevendo
      sem_wait(&escrita); // entra em espera se tiver escritor escrevendo
    }
    sem_post(&mutexL);

    sem_post(&fila); // incrementa o semaforo de leitura para liberar outras threads leitoras simultaneamente
    printf("Thread leitora %d lendo...\n", *id);
    for (int i = 0; i < 100000000; i++) {;}

    sem_wait(&mutexL);
    leitores--; // decrementa o numero de threads leitoras executando
    printf("Thread leitora %d terminou de ler \n", *id);
    if (leitores == 0) { // ultimo leitor sinaliza que escritores podem escrever
      sem_post(&escrita);
    }
    sem_post(&mutexL);
  }
}

void *escritor(void * arg) {
  int *id = (int *) arg;
  while (1) {
    sem_wait(&mutexE); // exclusao mutua para acesso a variavel escritores
    escritores++; // incrementa o numero de threads escritoras aguardando
    printf("%d escritor(es) aguardando \n", escritores);
    if (escritores == 1) { // se for o primeiro escritor aguardando, consome o semaforo de leitura para bloquear leitores
      sem_wait(&fila);
    }
    sem_post(&mutexE);

    sem_wait(&escrita); // esclusao mutua para escritores
    printf("Thread escritora %d escrevendo...\n", *id);
    sem_post(&escrita);

    sem_wait(&mutexE);
    escritores--;
    printf("Thread escritora %d terminou de escrever \n", *id);
    if (escritores == 0) { // quando nao tiverem mais escritores aguardando incrementa o semaforo da fila de leitura
      printf("Thread escritora %d vai liberar a fila de leitura porque nao ha escritores aguardando \n", *id);
      sem_post(&fila);
    }
    sem_post(&mutexE);

    sleep(1);
  }
}

// Funcao principal
int main(int argc, char *argv[]) {
  pthread_t tid[L + E]; // identificadores das threads
  int id[L + E];

  //inicia o semaforo binario
  sem_init(&mutexE, 0, 1);
  sem_init(&mutexL, 0, 1);
  sem_init(&escrita, 0, 1);
  sem_init(&fila, 0, 1);

  //cria as threads leitoras
  for (int i = 0; i < L; i++) {
    id[i] = i + 1;
    if (pthread_create(&tid[i], NULL, leitor, (void *)&id[i]))
      exit(-1);
  }

  //cria as threads escritoras
  for (int i = 0; i < E; i++) {
    id[i + L] = i + 1;
    if (pthread_create(&tid[i + L], NULL, escritor, (void *)&id[i + L]))
      exit(-1);
  }

  pthread_exit(NULL);

  return 0;
}