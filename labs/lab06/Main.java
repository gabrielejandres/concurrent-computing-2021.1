/*
     * Programa: Algoritmo concorrente para contar o numero de elementos pares em um vetor
     * Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
     * Disciplina: Computacao Concorrente - 2021.1
     * Modulo 2 - Laboratorio 6
     * Data: Setembro de 2021
*/
import java.util.Random;

// Classe da estrutura de dados (recurso) compartilhado entre as threads
class Counter {
  private int total = 0; // guarda o total de numeros pares no array (recurso compartilhado entre as threads)

  public synchronized void incrementTotal() {
    this.total++;
  }

  public synchronized int getTotal() {
    return this.total;
  }
}

// Classe que implementa a interface Runnable
class EvenNumbers implements Runnable {
  private int idThread; // identificador da thread
  private int nThreads; // total de threads
  private int[] array; // array de inteiros
  private Counter counter; // objeto compartilhado com outras threads

  // Construtor
  public EvenNumbers(int idThread, int nThreads, int[] array, Counter counter) {
    this.idThread = idThread;
    this.nThreads = nThreads;
    this.array = array;
    this.counter = counter;
  }

  // Metodo executado pela thread (estrategia: percorrer os elementos do array de forma intercalada)
  @Override
  public void run() {
    for (int i = idThread; i < array.length; i += nThreads) {
      if (array[i] % 2 == 0) this.counter.incrementTotal();
    }
  }
}

// Classe do metodo main
class Main {
  static final int SIZE = 1000000;
  static final int NTHREADS = 2;

  // Metodo para contar o total de numeros pares de forma sequencial
  static int countTotalSeq(int[] array) {
    int totalSeq = 0;
    for (int i = 0; i < array.length; i++) {
      if (array[i] % 2 == 0)
        totalSeq++;
    }
    return totalSeq;
  }

  // Metodo para conferir se a contagem sequencial e concorrente de numeros pares eh a mesma
  static void checkResult(Counter counter, int[] array) {
    int totalSeq = countTotalSeq(array);
    int totalConc = counter.getTotal();

    System.out.println("A versao concorrente encontrou " + totalConc + " numeros pares");
    System.out.println("A versao sequencial encontrou " + totalSeq + " numeros pares");

    if (totalSeq == totalConc) {
      System.out.println("O valor encontrado pela funcao concorrente esta correto!");
    } else {
      System.out.println("O valor encontrado pela funcao concorrente esta errado.");
    }
  }

  public static void main(String[] args) {
    Thread[] threads = new Thread[NTHREADS]; // reserva espaco para o vetor de threads
    int[] array = new int[SIZE]; // reserva espaco para o vetor de inteiros

    // Cria uma instancia do recurso compartilhado entre as threads
    Counter counter = new Counter();

    // Inicializa o array de inteiros
    Random rand = new Random();
    for (int i = 0; i < SIZE; i++) {
      array[i] = rand.nextInt();
    }

    // Transforma o objeto Runnable em Thread
    for (int i = 0; i < threads.length; i++) {
      threads[i] = new Thread(new EvenNumbers(i, NTHREADS, array, counter));
    }

    // Inicia as threads
    for (int i = 0; i < threads.length; i++) {
      threads[i].start();
    }

    // Espera pelo termino das threads
    for (int i = 0; i < threads.length; i++) {
      try {
        threads[i].join();
      } catch (InterruptedException e) {
        System.err.println(e);
        return;
      }
    }

    // Verifica a corretude do resultado
    checkResult(counter, array);
  }
}
