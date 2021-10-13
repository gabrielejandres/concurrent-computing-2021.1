#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define P 2
#define C 4

// globais
int n = 0; 
sem_t s, d; // s inicializado com 1 e d inicializado com 0

void retira_item(int *item) {
  printf("Retirando item... \n");
}

void consome_item(int item) {
  printf("Consumindo item... \n");
} 

void produz_item(int *item) {
  printf("Produzindo item... \n");
} 

void insere_item(int item) {
  printf("Inserindo item... \n");
}

void *cons(void *args) { 
  int item; 
  sem_wait(&d); // espera ter algo no buffer para consumir 
  while(1) { 
    sem_wait(&s); // exclusao mutua para a variavel n
    retira_item(&item); 
    n--; // decrementa o numero de itens no buffer
    sem_post(&s); 
    consome_item(item);
    sleep(1);
    if(n == 0) sem_wait(&d); 
  }
}

void *prod(void *args) {
  int item;
  while(1) {
    produz_item(&item);
    sem_wait(&s); // exclusao mutua para a variavel n
    insere_item(item);
    printf("Inserindo item... \n");
    n++; // incrementa o numero de itens no buffer
    if(n == 1) sem_post(&d);
    sleep(1);
    sem_post(&s);
  }
}

// Funcao principal
int main(int argc, char *argv[]) {
  pthread_t tid[P + C]; // identificadores das threads
  int id[P + C];

  // inicializacoes 
  sem_init(&s, 0, 1);
  sem_init(&d, 0, 0);

  for (int i = 0; i < P; i++) {
    id[i] = i + 1;
    if (pthread_create(&tid[i], NULL, prod, (void *) &id[i]))
      exit(-1);
  }

  for (int i = 0; i < C; i++) {
    id[i + P] = i + 1;
    if (pthread_create(&tid[i + P], NULL, cons, (void *) &id[i + P]))
      exit(-1);
  }

  pthread_exit(NULL);

  return 0;
}