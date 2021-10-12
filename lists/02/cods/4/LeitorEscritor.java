// Monitor que implementa a logica do padrao leitores/escritores
class Monitor {
  private int leitores, escritores, escritoresAguardando;

  // Construtor
  Monitor() {
    this.leitores = 0; // leitores lendo (0 ou mais)
    this.escritores = 0; // escritor escrevendo (0 ou 1)
    this.escritoresAguardando = 0; // indica a quantidade de escritores aguardando pra realizar escrita
  }

  // Entrada para leitores
  public synchronized void EntraLeitor(int id) {
    try {
      // enquanto tiver algum escritor escrevendo ou houverem novos escritores querendo escrever, as threads leitoras devem se bloquear
      while (this.escritores > 0 || this.escritoresAguardando > 0) { 
        System.out.println("Leitor " + id + " bloqueado...");
        wait(); // bloqueia pela condicao logica da aplicacao
      }
      this.leitores++; // registra que ha mais um leitor lendo
      System.out.println("Leitor " + id + " lendo...");
    } catch (InterruptedException e) {
        System.err.println(e);
    }
  }

  // Saida para leitores
  public synchronized void SaiLeitor(int id) {
    this.leitores--; // registra que um leitor saiu
    if (this.leitores == 0) this.notify(); // libera escritor no caso de não haverem mais leitores (caso exista escritor bloqueado)
    System.out.println("Leitor " + id + " saindo...");
  }

  // Entrada para escritores
  public synchronized void EntraEscritor(int id) {
    try {
      this.escritoresAguardando++; // indica que ha um novo escritor querendo escrever
      System.out.println("Escritor " + id + " quer escrever...");
      System.out.println(this.escritoresAguardando + " escritores aguardando para escrever...");
      while ((this.leitores > 0) || (this.escritores > 0)) {
        System.out.println("Escritor " + id + " bloqueado...");
        wait(); // bloqueia pela condicao logica da aplicacao
      }
      this.escritoresAguardando--; // indica que nao esta mais aguardando pois ira escrever
      this.escritores++; // registra que ha um escritor escrevendo
      System.out.println("Escritor " + id + " escrevendo...");
    } catch (InterruptedException e) {
        System.err.println(e);
    }
  }

  // Saida para escritores
  public synchronized void SaiEscritor(int id) {
    this.escritores--; // registra que o escritor saiu
    notifyAll(); // libera leitores e escritores (caso existam leitores ou escritores bloqueados)
    System.out.println("Escritor " + id + " saindo...");
  }
}

// --- Aplicacao de exemplo ---
// Leitor
class Leitor extends Thread {
  int id; // identificador da thread
  int delay; // atraso bobo
  Monitor monitor; // objeto monitor para coordenar a lógica de execução das threads

  // Construtor
  Leitor(int id, int delayTime, Monitor m) {
    this.id = id;
    this.delay = delayTime;
    this.monitor = m;
  }

  // Método executado pela thread
  public void run() {
    double j = 777777777.7, i;
    try {
      for (;;) {
        this.monitor.EntraLeitor(this.id);
        for (i = 0; i < 100000000; i++) {
          j = j / 2;
        } // ...loop bobo para simbolizar o tempo de leitura
        this.monitor.SaiLeitor(this.id);
        sleep(this.delay);
      }
    } catch (InterruptedException e) {
      return;
    }
  }
}

// Escritor
class Escritor extends Thread {
  int id; // identificador da thread
  int delay; // atraso bobo...
  Monitor monitor; // objeto monitor para coordenar a lógica de execução das threads

  // Construtor
  Escritor(int id, int delayTime, Monitor m) {
    this.id = id;
    this.delay = delayTime;
    this.monitor = m;
  }

  // Método executado pela thread
  public void run() {
    double j = 777777777.7, i;
    try {
      for (;;) {
        this.monitor.EntraEscritor(this.id);
        for (i = 0; i < 100000000; i++) {
          j = j / 2;
        } // ...loop bobo para simbolizar o tempo de escrita
        this.monitor.SaiEscritor(this.id);
        sleep(this.delay); // atraso bobo...
      }
    } catch (InterruptedException e) {
      return;
    }
  }
}

// Classe principal
class LeitorEscritor {
  static final int L = 4;
  static final int E = 2;

  public static void main(String[] args) {
    int i;
    Monitor monitor = new Monitor(); // Monitor (objeto compartilhado entre leitores e escritores)
    Leitor[] l = new Leitor[L]; // Threads leitores
    Escritor[] e = new Escritor[E]; // Threads escritores

    for (i = 0; i < L; i++) {
      l[i] = new Leitor(i + 1, (i + 1) * 500, monitor);
      l[i].start();
    }

    for (i = 0; i < E; i++) {
      e[i] = new Escritor(i + 1, (i + 1) * 500, monitor);
      e[i].start();
    }
  }
}
