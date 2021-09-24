#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

/* Variaveis globais */
int bloqueadas = 0;
pthread_mutex_t x_mutex;
pthread_cond_t x_cond;
int nthreads;
int *vetor;

void seq(int vetor[], int n) {
  int vet[n];

  // copia do vetor de entrada
  for(int i = 0; i < n; i++) {
    vet[i] = vetor[i];
  }

  // calculo
  for(int i = 1; i < n; i++) {
    vet[i] = vet[i] + vet[i-1];
  }

  printf("SEQUENCIAL: \n");
  for (int j = 0; j < n; j++) {
    printf("%d \n", vet[j]);
  }
}

/* Funcao barreira */
void barreira(int nthreads, int id) {
  pthread_mutex_lock(&x_mutex);
  if (bloqueadas == (nthreads - 1)) {
    // Quando a ultima thread chegar na barreira ela pode sinalizar que as outras que estao aguardando podem prosseguir
    printf("Thread %d liberou a barreira...\n", id);
    pthread_cond_broadcast(&x_cond);
    bloqueadas = 0;
  }
  else {
    bloqueadas++;
    // Se nao for a ultima thread vai esperar
    printf("Thread %d parou na barreira...\n", id);
    pthread_cond_wait(&x_cond, &x_mutex);
  }
  pthread_mutex_unlock(&x_mutex);
}
/* Funcao das threads */
void *tarefa(void *arg) {
  int id = *(int *) arg;
  int salto;
  int aux;
  for (salto = 1; salto < nthreads; salto *= 2) {
    if (id >= salto) {
      printf("Thread %d: salto %d\n", id, salto);
      aux = vetor[id - salto];
      printf("aux = vetor[%d] = %d \n", id-salto, aux);
      barreira(nthreads - salto, id);
      vetor[id] = aux + vetor[id];
      printf("vetor[%d] = %d \n", id, vetor[id]);
      // barreira(nthreads - salto, id);
    }
    else
      break;
  }
  pthread_exit(NULL);
}

/* Funcao principal */
int main(int argc, char *argv[]) {
  pthread_t *threads; // identificadores das threads no sistema
  int *id;

  /* Inicializa o mutex (lock de exclusao mutua) e a variavel de condicao */
  pthread_mutex_init(&x_mutex, NULL);
  pthread_cond_init(&x_cond, NULL);
  
  /* Recebe os parametros de entrada (tamanho do vetor == n umero de threads) */
  if (argc < 2) {
    printf("Digite: %s <numero de threads>\n", argv[0]);
    return 1;
  }
  
  /* Inicia as variaveis globais e carrega o vetor de entrada */
  nthreads = atoi(argv[1]);

  threads = (pthread_t*) malloc(sizeof(pthread_t)*nthreads);
  if (threads == NULL) {
    puts("Erro de alocacao de memoria");
    return 2;
  }

  id = (int*) malloc(sizeof(int)*nthreads);
  if (id == NULL) {
    puts("Erro de alocacao de memoria");
    return 2;
  }

  vetor = (int *) malloc(sizeof(int) * nthreads);
  if (vetor == NULL) {
    printf("Erro de alocacao de memoria para vetor");
    return 2;
  }

  for (int j = 0; j < nthreads; j++) {
    vetor[j] = j + 1;
  }
  // vetor[0] = 1;
  // vetor[1] = 4;
  // vetor[2] = -1;
  // vetor[3] = 7;

  seq(vetor, nthreads);
  
  /* Cria as threads */
  for (int i = 0; i < nthreads; i++) {
    id[i] = i;
    pthread_create(threads + i, NULL, tarefa, (void *) (id + i));
  }

  /* Espera todas as threads completarem */
  for (int i = 0; i < nthreads; i++) {
    pthread_join(*(threads + i), NULL);
  }

  printf("CONCORRENTE: \n");
  for (int j = 0; j < nthreads; j++) {
    printf("%d \n", vetor[j]);
  }

  /* Armazena o vetor de saida, libera variáveis e encerra */
  free(vetor);
  
  return 0;
}