import java.util.LinkedList;

class FilaTarefas {
  private int nThreads; // numero de threads
  private MyPoolThreads[] threads; 
  private LinkedList<Runnable> queue; // similar a um vetor de objetos Runnable (tarefas)
  private boolean shutdown; // indica o encerramento do pool

  // Construtor da classe
  public FilaTarefas(int nThreads) {
    this.shutdown = false; // no inicio, nao quero encerrar o pool
    this.nThreads = nThreads; // numero de threads do pool
    queue = new LinkedList<Runnable>(); // fila de objetos runnable (tarefas)
    threads = new MyPoolThreads[nThreads]; // array de threads

    // Criacao e armazenamento das threads
    for (int i = 0; i < nThreads; i++) {
      threads[i] = new MyPoolThreads(); // cria uma nova thread
      threads[i].start(); // inicia a thread
    }
  }

  // Escalona uma tarefa para execucao pelo pool
  public void execute(Runnable r) {
    synchronized (queue) {
      if (this.shutdown) return; // se tiver encerrado o pool, nao faz nada
      queue.addLast(r); // inclui um novo elemento (tarefa) na lista ’queue’
      queue.notify(); // notifica as threads que existe um novo elemento na lista
    }
  }

  // Encerra o pool depois que todas as tarefas escalonadas foram finalizadas
  public void shutdown() {
    synchronized (queue) {
      this.shutdown = true; // indica o encerramento do pool
      queue.notifyAll();
    }

    // faz o join das threads
    for (int i = 0; i < nThreads; i++) 
      try {
        threads[i].join();
      } catch (InterruptedException e) {
        return;
      }
  }

  // O pool de threads permite construir aplicacoes com alocacao dinamica de tarefas para as threads
  private class MyPoolThreads extends Thread {

    @Override
    public void run() {
      Runnable r;
      while (true) {
        synchronized (queue) {
          // Verifica se a lista esta vazia...
          while (queue.isEmpty() && (!shutdown)) {
            try {
              queue.wait(); // se a lista tiver vazia e nao tiver sinal de encerramento aguarda as tarefas
            } catch (InterruptedException ignored) {}
          }
          if (queue.isEmpty() && shutdown) return; // se a lista esta vazia e ha sinal de encerramento acabaram as tarefas
          r = (Runnable) queue.removeFirst(); // retira o primeiro elemento da lista e o retorna
        }
        try {
          r.run();
        } catch (RuntimeException e) {}
      }
    }
  }
}

class Tarefa implements Runnable {
  private int id;  
  
  public Tarefa(int id){
      this.id = id;
  }

  @Override
  public void run() {
      System.out.println("Tarefa " + this.id +" executada por " + Thread.currentThread().getName());
  }  
}

class Main {
  public static void main(String args[]) {
    FilaTarefas tarefas = new FilaTarefas(10); 
    for (int i = 0; i < 100; i++) {
      tarefas.execute(new Tarefa(i));  
    }
    tarefas.shutdown();
 } 
}
