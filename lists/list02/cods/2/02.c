#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

long long int contador = 0;
pthread_mutex_t mutex;
pthread_cond_t cond;
bool novo_multiplo = false;

void *T1 (void *arg) {
  while(1) {
    pthread_mutex_lock(&mutex);
    // FazAlgo(contador);
    contador++;
    if (contador % 100 == 0) {
      novo_multiplo = true;
      pthread_cond_signal(&cond);
      pthread_cond_wait(&cond, &mutex);
    }
    pthread_mutex_unlock(&mutex);
  }

  pthread_exit(NULL);
}

void *T2 (void *arg) {
  while(1) {
    pthread_mutex_lock(&mutex);
    if (contador % 100 != 0 || !novo_multiplo) {
      pthread_cond_wait(&cond, &mutex);
    }
    printf("%lld \n", contador);
    novo_multiplo = false;
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&mutex);
  }

  pthread_exit(NULL);
}

int main(void) {
  // variaveis auxiliares
  int i;

  // identificadores das threads
  pthread_t tid[2];
  int *id[2];

  // inicializa as variaveis de sincronizacao
  pthread_mutex_init(&mutex, NULL);
  pthread_cond_init(&cond, NULL);

  // cria as threads
  pthread_create(&tid[0], NULL, T1, (void *) id[0]);
  pthread_create(&tid[1], NULL, T2, (void *) id[1]);

  pthread_exit(NULL);

  return 0;
}