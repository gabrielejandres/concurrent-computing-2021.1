# Relatório | Laboratório 03 | Computação Concorrente
*Análise de desempenho da solução concorrente para encontrar o maior e o menor elemento de um vetor.*

## Tabela de Conteúdo

 1. [Tempos de execução](#tempos-de-execução)
 2. [Ganho de desempenho](#ganho-de-desempenho)

## Tempos de execução

### Dimensão 10<sup>5</sup>

| Solução | Tempo de execução |
| --- | --- |
| **Sequencial** | 0.000316s |
| **2 Threads** | 0.001197s |
| **4 Threads** | 0.001270s |

### Dimensão 10<sup>7</sup>

| Solução | Tempo de execução |
| --- | --- |
| **Sequencial** | 0.030206s |
| **2 Threads** | 0.015171s |
| **4 Threads** | 0.014056s |

### Dimensão 10<sup>9</sup>

| Solução | Tempo de execução |
| --- | --- |
| **Sequencial** | 7.999201s |
| **2 Threads** | 4.354146s |
| **4 Threads** | 3.459456s |

## Ganho de desempenho

### Dimensão 10<sup>5</sup>

| N° de Threads | Aceleração |
| --- | --- |
| **2 Threads** | 0.26 |
| **4 Threads** | 0.24 |

### Dimensão 10<sup>7</sup>

| N° de Threads | Aceleração |
| --- | --- |
| **2 Threads** | 1.99 |
| **4 Threads** | 2.15 |

### Dimensão 10<sup>9</sup>

| N° de Threads | Aceleração |
| --- | --- |
| **2 Threads** | 1.84 |
| **4 Threads** | 2.31 |

