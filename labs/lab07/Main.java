/*
	* Programa: Aplicacao concorrente usando o padrao leitores/escritores para acessar uma variavel compartilhada
	* Aluna: Gabriele Jandres Cavalcanti | DRE: 119159948
	* Disciplina: Computacao Concorrente - 2021.1
	* Modulo 2 - Laboratorio 7
	* Data: Setembro de 2021
*/

// Monitor que implementa a logica do padrao leitores/escritores
class Monitor {
	private int reading, writing;
	private int centralElement = 0; // recurso compartilhado entre as threads

	// Getter para a variavel compartilhada
	public synchronized int getCentralElement() {
		return this.centralElement;
	}

	// Setter para a variavel compartilhada
	public synchronized void setCentralElement(int number) {
		this.centralElement = number;
	}

	// Construtor
	Monitor() {
		this.reading = 0; // leitores lendo (0 ou mais)
		this.writing = 0; // escritor escrevendo (0 ou 1)
	}

	// Entrada para leitores
	public synchronized void EnterReader(int id) {
		try {
			while (this.writing > 0) {
				System.out.println("le.leitorBloqueado(" + id + ")");
				wait(); // bloqueia pela condicao logica da aplicacao
			}
			this.reading++; // registra que ha mais um leitor lendo
			System.out.println("le.leitorLendo(" + id + ")");
		} catch (InterruptedException e) {
			System.err.println(e);
		}
	}

	// Saida para leitores
	public synchronized void LeaveReader(int id) {
		this.reading--; // registra que um leitor saiu
		if (this.reading == 0)
			this.notify(); // libera escritor (caso exista escritor bloqueado)
		System.out.println("le.leitorSaindo(" + id + ")");
	}

	// Entrada para escritores
	public synchronized void EnterWriter(int id) {
		try {
			while ((this.reading > 0) || (this.writing > 0)) {
				System.out.println("le.escritorBloqueado(" + id + ")");
				wait(); // bloqueia pela condicao logica da aplicacao
			}
			this.writing++; // registra que ha um escritor escrevendo
			System.out.println("le.escritorEscrevendo(" + id + ")");
		} catch (InterruptedException e) {
			System.err.println(e);
		}
	}

	// Saida para escritores
	public synchronized void LeaveWriter(int id) {
		this.writing--; // registra que o escritor saiu
		notifyAll(); // libera leitores e escritores (caso existam leitores ou escritores bloqueados)
		System.out.println("le.escritorSaindo(" + id + ")");
	}
}

// Thread leitora
class Reader extends Thread {
	int id; // identificador da thread
	int delay; // atraso
	Monitor monitor; // objeto monitor para coordenar a lógica de execução das threads

	// Construtor
	Reader(int id, int delayTime, Monitor m) {
		this.id = id;
		this.delay = delayTime;
		this.monitor = m;
	}

	// Metodo auxiliar para verificar se um numero eh primo
	public void isPrimeNumber(int number) {
		if (number == 0) {
			System.out.println("# O elemento central tem valor " + number + " e nao eh primo");
			return;
		}

		for (int i = 2; i < number; i++) {
			if (number % i == 0) {
				System.out.println("# O elemento central tem valor " + number + " e nao eh primo");
				return;
			}
		}

		System.out.println("# O elemento central tem valor " + number + " e eh primo");
	}

	// Método executado pela thread
	@Override
	public void run() {
		try {
			for (int i = 0; i < Main.INTERACTIONS; i++) {
				this.monitor.EnterReader(this.id);
				isPrimeNumber(this.monitor.getCentralElement());
				System.out.println("# Thread leitora " + this.id + " leu");
				this.monitor.LeaveReader(this.id);
				sleep(this.delay);
			}
		} catch (InterruptedException e) {
			System.err.println(e);
			return;
		}
	}
}

// Thread escritora
class Writer extends Thread {
	int id; // identificador da thread
	int delay; // atraso
	Monitor monitor; // objeto monitor para coordenar a lógica de execução das threads

	// Construtor
	Writer(int id, int delayTime, Monitor m) {
		this.id = id;
		this.delay = delayTime;
		this.monitor = m;
	}

	// Método executado pela thread
	public void run() {
		try {
			for (int i = 0; i < Main.INTERACTIONS; i++) {
				this.monitor.EnterWriter(this.id);
				this.monitor.setCentralElement(this.id);
				System.out.println("# Thread escritora " + this.id + " escreveu: " + this.id);
				this.monitor.LeaveWriter(this.id);
				sleep(this.delay);
			}
		} catch (InterruptedException e) {
			System.err.println(e);
			return;
		}
	}
}

// Thread leitora/escritora
class ReaderAndWriter extends Thread {
	int id; // identificador da thread
	int delay; // atraso
	Monitor monitor; // objeto monitor para coordenar a lógica de execução das threads

	// Construtor
	ReaderAndWriter(int id, int delayTime, Monitor m) {
		this.id = id;
		this.delay = delayTime;
		this.monitor = m;
	}

	// Metodo auxiliar para verificar se um numero eh par ou impar
	public void checkParity(int number) {
		if (number % 2 == 0) {
			System.out.println("# O elemento central tem valor " + number + " e eh par");
			return;
		}
		System.out.println("# O elemento central tem valor " + number + " e eh impar");
	}

	// Método executado pela thread
	@Override
	public void run() {
		try {
			for (int i = 0; i < Main.INTERACTIONS; i++) {
				// leitura (mesma logica da thread leitora)
				this.monitor.EnterReader(this.id);
				checkParity(this.monitor.getCentralElement());
				System.out.println("# Thread leitora e escritora " + this.id + " leu");
				this.monitor.LeaveReader(this.id);
				// escrita (mesma logica da thread escritora)
				this.monitor.EnterWriter(this.id);
				this.monitor.setCentralElement(2 * this.monitor.getCentralElement());
				System.out.println("# Thread leitora e escritora " + this.id + " escreveu: " + this.monitor.getCentralElement());
				this.monitor.LeaveWriter(this.id);

				sleep(this.delay);
			}
		} catch (InterruptedException e) {
			System.err.println(e);
			return;
		}
	}
}

// Classe principal
class Main {
	public static final int INTERACTIONS = 10; // total de interacoes das threads (limite para nao executar infinitamente)
	private static final int READERS = 5; // total de threads leitoras
	private static final int WRITERS = 5; // total de threads escritoras
	private static final int RW = 5; // total de threads leitoras e escritoras

	public static void main(String[] args) {
		Monitor monitor = new Monitor(); // Monitor (objeto compartilhado entre leitores e escritores)
		Reader[] readers = new Reader[READERS]; // Threads leitoras
		Writer[] writers = new Writer[WRITERS]; // Threads escritoras
		ReaderAndWriter[] readersAndWriters = new ReaderAndWriter[RW]; // Threads leitoras e escritoras

		// Inicia o log de saida
		System.out.println("import verificaLE");
		System.out.println("le = verificaLE.LE()");

		// Cria os leitores
		for (int i = 0; i < READERS; i++) {
			readers[i] = new Reader(i + 1, (i + 1) * 500, monitor);
			readers[i].start();
		}

		// Cria os escritores
		for (int i = 0; i < WRITERS; i++) {
			writers[i] = new Writer(i + 1, (i + 1) * 500, monitor);
			writers[i].start();
		}

		// Cria os leitores/escritores
		for (int i = 0; i < RW; i++) {
			readersAndWriters[i] = new ReaderAndWriter(i + 1, (i + 1) * 500, monitor);
			readersAndWriters[i].start();
		}
	}
}