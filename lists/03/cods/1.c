#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define A 5
#define B 5
#define C 5

// globais
int a = 0, b = 0, c = 0; // numero de threads A, B e C usando o recurso, respectivamente
sem_t emA, emB, emC; // semaforos para exclusao mutua
sem_t rec; // semaforo para sincronizacao logica

// funcao executada pelas As
void *func_A() {
  while (1) {
    sem_wait(&emA); // exclusao mutua da variavel a
    a++;
    if (a == 1) { // se for a primeira, vai aguardar pelo recurso
      sem_wait(&rec);
    }
    sem_post(&emA);

    printf("A executando com a = %d... \n", a);
    sleep(1);
    // SC: usa o recurso

    sem_wait(&emA); // exclusao mutua da variavel a
    a--;
    printf("Valor de a = %d \n", a);
    if (a == 0) { // se for a ultima thread do tipo A a executar libera o recurso
      sem_post(&rec);
    }
    sem_post(&emA);
  }
}

//funcao executada pelas Bs
void *func_B() {
  while (1) {
    sem_wait(&emB);
    b++;
    if(b == 1) {
      sem_wait(&rec);
    }
    sem_post(&emB);

    printf("B executando com b = %d... \n", b);
    sleep(1);
    // SC: usa o recurso

    sem_wait(&emB);
    b--;
    printf("Valor de b = %d \n", b);
    if (b == 0) { // se for a ultima thread do tipo B a executar libera o recurso
      sem_post(&rec);
    }
    sem_post(&emB);
  }
}

//funcao executada pelas Cs
void *func_C () {
  while(1) {
    sem_wait(&emC);
    c++;
    if(c == 1) {
      sem_wait(&rec);
    }
    sem_post(&emC);

    printf("C executando com c = %d... \n", c);
    sleep(1);
    // SC: usa o recurso

    sem_wait(&emC);
    c--;
    printf("Valor de c = %d \n", c);
    if(c == 0) { // se for a ultima thread do tipo C a executar libera o recurso
      sem_post(&rec);
    }
    sem_post(&emC);
  }
}

// Funcao principal
int main(int argc, char *argv[]) {
  //identificadores das threads
  pthread_t tid[A + B + C];
  int id[A + B + C];

  // inicializacoes 
  sem_init(&emA, 0, 1);
  sem_init(&emB, 0, 1);
  sem_init(&emC, 0, 1);
  sem_init(&rec, 0, 1);

  for (int i = 0; i < A; i++) {
    id[i] = i + 1;
    if (pthread_create(&tid[i], NULL, func_A, (void *)&id[i]))
      exit(-1);
  }

  for (int i = 0; i < B; i++) {
    id[i + B] = i + 1;
    if (pthread_create(&tid[i + b], NULL, func_B, (void *)&id[i + B]))
      exit(-1);
  }

  for (int i = 0; i < C; i++) {
    id[i + B + C] = i + 1;
    if (pthread_create(&tid[i + b + c], NULL, func_C, (void *)&id[i + B + C]))
      exit(-1);
  }

  pthread_exit(NULL);

  return 0;
}