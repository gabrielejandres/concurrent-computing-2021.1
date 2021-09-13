import verificaLE
le = verificaLE.LE()
le.leitorLendo(1)
le.leitorLendo(2)
# O elemento central tem valor 0 e nao eh primo
# O elemento central tem valor 0 e nao eh primo
# Thread leitora 1 leu
# Thread leitora 2 leu
le.leitorSaindo(1)
le.leitorSaindo(2)
le.leitorLendo(3)
le.leitorLendo(4)
# O elemento central tem valor 0 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
# O elemento central tem valor 0 e nao eh primo
le.leitorLendo(5)
# O elemento central tem valor 0 e nao eh primo
# Thread leitora 5 leu
le.leitorSaindo(5)
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(1)
le.escritorBloqueado(3)
# Thread escritora 1 escreveu: 1
le.escritorBloqueado(2)
le.escritorSaindo(1)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorBloqueado(5)
le.escritorBloqueado(2)
le.escritorBloqueado(3)
le.leitorBloqueado(2)
le.leitorBloqueado(1)
le.escritorSaindo(4)
le.leitorLendo(3)
le.leitorLendo(1)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 1 leu
le.leitorLendo(4)
# O elemento central tem valor 4 e eh par
le.leitorLendo(2)
# Thread leitora e escritora 4 leu
le.escritorBloqueado(3)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 2 leu
le.escritorBloqueado(2)
le.escritorBloqueado(5)
le.leitorSaindo(2)
le.leitorSaindo(4)
le.escritorBloqueado(4)
# O elemento central tem valor 4 e eh par
le.leitorSaindo(1)
# Thread leitora e escritora 3 leu
le.escritorBloqueado(1)
le.leitorLendo(5)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 5 leu
le.leitorSaindo(3)
le.escritorBloqueado(3)
le.escritorBloqueado(2)
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 8
le.escritorBloqueado(3)
le.escritorSaindo(5)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorBloqueado(2)
le.escritorBloqueado(3)
le.escritorBloqueado(1)
le.escritorBloqueado(4)
le.escritorBloqueado(5)
le.escritorBloqueado(2)
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorBloqueado(5)
le.escritorBloqueado(4)
le.escritorBloqueado(1)
le.escritorBloqueado(3)
le.escritorBloqueado(2)
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 4
le.escritorBloqueado(3)
le.escritorBloqueado(1)
le.escritorBloqueado(4)
le.escritorBloqueado(5)
le.escritorSaindo(2)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorBloqueado(4)
le.escritorBloqueado(1)
le.escritorBloqueado(3)
le.escritorSaindo(5)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 10
le.escritorBloqueado(1)
le.escritorBloqueado(4)
le.escritorSaindo(3)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 20
le.escritorBloqueado(1)
le.escritorSaindo(4)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 40
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.leitorBloqueado(1)
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 2
le.escritorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.leitorBloqueado(2)
le.leitorBloqueado(2)
le.escritorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 2 leu
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.escritorBloqueado(2)
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 4
le.escritorSaindo(2)
le.leitorLendo(1)
# O elemento central tem valor 4 e nao eh primo
le.escritorBloqueado(1)
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 2
le.escritorSaindo(1)
le.leitorLendo(3)
# O elemento central tem valor 2 e eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
le.leitorBloqueado(1)
le.leitorBloqueado(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorLendo(1)
# O elemento central tem valor 3 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(3)
le.escritorBloqueado(3)
le.leitorSaindo(1)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 6
le.escritorSaindo(3)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 2
le.escritorSaindo(1)
le.escritorEscrevendo(4)
le.leitorBloqueado(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.leitorLendo(4)
# O elemento central tem valor 4 e nao eh primo
le.leitorLendo(4)
# Thread leitora 4 leu
le.escritorBloqueado(2)
# O elemento central tem valor 4 e eh par
le.leitorLendo(2)
# Thread leitora e escritora 4 leu
le.leitorLendo(2)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 2 leu
le.leitorSaindo(4)
# O elemento central tem valor 4 e eh par
le.escritorBloqueado(4)
# Thread leitora e escritora 2 leu
le.leitorSaindo(4)
le.leitorSaindo(2)
le.escritorBloqueado(2)
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 4
le.escritorBloqueado(4)
le.escritorSaindo(2)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 8
le.escritorSaindo(4)
le.leitorLendo(1)
# O elemento central tem valor 8 e nao eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 2
le.escritorSaindo(1)
le.leitorLendo(5)
# O elemento central tem valor 2 e eh primo
# Thread leitora 5 leu
le.leitorLendo(5)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 4
le.escritorSaindo(5)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
le.leitorLendo(1)
# O elemento central tem valor 5 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.leitorLendo(1)
le.escritorBloqueado(1)
# O elemento central tem valor 5 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 10
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.escritorSaindo(1)
le.leitorLendo(3)
# O elemento central tem valor 1 e eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.leitorLendo(3)
le.escritorBloqueado(2)
le.leitorLendo(1)
# O elemento central tem valor 3 e eh primo
# Thread leitora 1 leu
le.leitorLendo(2)
# O elemento central tem valor 3 e eh primo
le.leitorSaindo(1)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorLendo(2)
# Thread leitora 2 leu
le.leitorSaindo(3)
le.escritorBloqueado(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 6
le.escritorBloqueado(2)
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorBloqueado(3)
le.escritorSaindo(2)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 4
le.escritorSaindo(3)
le.leitorLendo(1)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 1 leu
le.escritorBloqueado(1)
le.leitorSaindo(1)
le.escritorEscrevendo(1)
le.escritorBloqueado(1)
# Thread leitora e escritora 1 escreveu: 8
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.leitorBloqueado(1)
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 2
le.escritorSaindo(1)
le.leitorLendo(4)
# O elemento central tem valor 2 e eh primo
le.escritorBloqueado(4)
# Thread leitora 4 leu
le.leitorLendo(4)
# O elemento central tem valor 2 e eh par
le.leitorSaindo(4)
# Thread leitora e escritora 4 leu
le.leitorSaindo(4)
le.escritorEscrevendo(4)
le.escritorBloqueado(4)
# Thread leitora e escritora 4 escreveu: 4
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.leitorLendo(1)
# O elemento central tem valor 4 e nao eh primo
le.leitorLendo(2)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 2 leu
le.escritorBloqueado(2)
le.leitorLendo(2)
# O elemento central tem valor 4 e eh par
le.leitorSaindo(2)
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorBloqueado(2)
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 4
le.escritorSaindo(2)
le.leitorLendo(1)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 1 leu
le.escritorBloqueado(1)
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 8
le.escritorBloqueado(1)
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.escritorSaindo(1)
le.leitorLendo(3)
# O elemento central tem valor 1 e eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.leitorLendo(1)
# O elemento central tem valor 3 e eh primo
# Thread leitora 1 leu
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorSaindo(1)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 6
le.escritorSaindo(3)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu: 1
le.leitorBloqueado(1)
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu: 2
le.escritorSaindo(1)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.leitorBloqueado(5)
le.leitorBloqueado(5)
le.escritorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 5 e eh primo
# Thread leitora 5 leu
le.leitorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 5 e eh impar
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 10
le.escritorSaindo(5)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 2 leu
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.escritorBloqueado(2)
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 4
le.escritorSaindo(2)
le.leitorLendo(3)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.leitorLendo(4)
le.escritorBloqueado(4)
le.leitorLendo(4)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 4 leu
le.escritorBloqueado(3)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.escritorBloqueado(4)
le.leitorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 8
le.escritorBloqueado(3)
le.escritorSaindo(4)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorSaindo(2)
le.leitorLendo(3)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 2 leu
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.escritorBloqueado(2)
le.leitorSaindo(2)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 4
le.escritorBloqueado(2)
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 8
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 4
le.escritorSaindo(2)
le.leitorLendo(5)
le.leitorLendo(5)
# O elemento central tem valor 4 e nao eh primo
# O elemento central tem valor 4 e eh par
le.escritorBloqueado(5)
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.escritorBloqueado(5)
# Thread leitora 5 leu
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 10
le.escritorSaindo(5)
le.leitorLendo(3)
# O elemento central tem valor 10 e nao eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 6
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.leitorBloqueado(4)
le.escritorBloqueado(4)
le.leitorBloqueado(4)
le.escritorSaindo(2)
le.leitorLendo(4)
# O elemento central tem valor 2 e eh primo
# Thread leitora 4 leu
le.escritorBloqueado(4)
le.leitorLendo(4)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 4 leu
le.leitorSaindo(4)
le.leitorSaindo(4)
le.escritorEscrevendo(4)
le.escritorBloqueado(4)
# Thread leitora e escritora 4 escreveu: 4
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.leitorLendo(2)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 8
le.escritorSaindo(2)
le.leitorLendo(3)
# O elemento central tem valor 8 e nao eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu: 2
le.escritorSaindo(2)
le.leitorLendo(3)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
# O elemento central tem valor 2 e eh par
le.leitorSaindo(2)
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 4
le.escritorSaindo(3)
le.leitorLendo(2)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu: 8
le.escritorSaindo(2)
le.leitorLendo(5)
# O elemento central tem valor 8 e nao eh primo
le.escritorBloqueado(5)
le.leitorLendo(5)
# O elemento central tem valor 8 e eh par
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.escritorBloqueado(5)
# Thread leitora 5 leu
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 10
le.escritorSaindo(5)
le.escritorEscrevendo(4)
le.leitorBloqueado(4)
le.leitorBloqueado(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.leitorLendo(4)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 4 leu
le.leitorLendo(4)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.escritorBloqueado(4)
le.leitorSaindo(4)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 8
le.escritorSaindo(4)
le.leitorLendo(3)
# O elemento central tem valor 8 e nao eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 6
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 6 e nao eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.leitorLendo(4)
# O elemento central tem valor 6 e nao eh primo
# Thread leitora 4 leu
le.escritorBloqueado(3)
le.escritorBloqueado(4)
le.leitorLendo(4)
# O elemento central tem valor 6 e eh par
# Thread leitora e escritora 4 leu
le.leitorSaindo(4)
le.escritorBloqueado(4)
le.leitorSaindo(4)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 6
le.escritorBloqueado(4)
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.leitorLendo(3)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 8
le.escritorSaindo(3)
le.leitorLendo(5)
le.leitorLendo(5)
# O elemento central tem valor 8 e nao eh primo
le.escritorBloqueado(5)
# Thread leitora 5 leu
le.leitorSaindo(5)
# O elemento central tem valor 8 e eh par
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 16
le.escritorBloqueado(5)
le.escritorSaindo(5)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
le.leitorLendo(3)
# O elemento central tem valor 5 e eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu: 3
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu: 6
le.escritorSaindo(3)
le.leitorLendo(4)
# O elemento central tem valor 6 e nao eh primo
le.leitorLendo(4)
# O elemento central tem valor 6 e eh par
# Thread leitora e escritora 4 leu
# Thread leitora 4 leu
le.escritorBloqueado(4)
le.leitorSaindo(4)
le.leitorSaindo(4)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 12
le.escritorBloqueado(4)
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 5 e eh primo
# Thread leitora 5 leu
le.leitorLendo(5)
# O elemento central tem valor 5 e eh impar
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 10
le.escritorSaindo(5)
le.leitorLendo(4)
le.leitorLendo(4)
# O elemento central tem valor 10 e eh par
# Thread leitora e escritora 4 leu
le.escritorBloqueado(4)
le.leitorSaindo(4)
le.escritorBloqueado(4)
# O elemento central tem valor 10 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 8
le.escritorSaindo(4)
le.escritorEscrevendo(5)
le.leitorBloqueado(5)
le.leitorBloqueado(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 5 e eh impar
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 10
le.escritorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 10 e nao eh primo
# Thread leitora 5 leu
le.leitorSaindo(5)
le.leitorLendo(4)
# O elemento central tem valor 10 e eh par
le.leitorLendo(4)
# O elemento central tem valor 10 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
# Thread leitora e escritora 4 leu
le.escritorBloqueado(4)
le.leitorSaindo(4)
le.escritorEscrevendo(4)
# Thread leitora e escritora 4 escreveu: 20
le.escritorBloqueado(4)
le.escritorSaindo(4)
le.escritorEscrevendo(4)
# Thread escritora 4 escreveu: 4
le.escritorSaindo(4)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.leitorBloqueado(5)
le.leitorBloqueado(5)
le.escritorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 5 e eh impar
# Thread leitora e escritora 5 leu
le.leitorLendo(5)
# O elemento central tem valor 5 e eh primo
# Thread leitora 5 leu
le.leitorSaindo(5)
le.escritorBloqueado(5)
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 10
le.escritorSaindo(5)
le.leitorLendo(5)
# O elemento central tem valor 10 e eh par
le.escritorBloqueado(5)
le.leitorLendo(5)
# O elemento central tem valor 10 e nao eh primo
# Thread leitora 5 leu
le.leitorSaindo(5)
# Thread leitora e escritora 5 leu
le.leitorSaindo(5)
le.escritorEscrevendo(5)
# Thread leitora e escritora 5 escreveu: 20
le.escritorBloqueado(5)
le.escritorSaindo(5)
le.escritorEscrevendo(5)
# Thread escritora 5 escreveu: 5
le.escritorSaindo(5)
