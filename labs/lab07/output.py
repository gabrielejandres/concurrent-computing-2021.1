import verificaLE
le = verificaLE.LE()
le.leitorLendo(1)
le.leitorLendo(2)
# O elemento central tem valor 0 e nao eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.leitorLendo(3)
# O elemento central tem valor 0 e nao eh primo
# O elemento central tem valor 0 e nao eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
# Thread leitora 3 leu
le.leitorSaindo(3)
le.leitorLendo(4)
# O elemento central tem valor 0 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorSaindo(1)
le.escritorEscrevendo(2)
le.escritorBloqueado(3)
le.leitorBloqueado(1)
le.leitorBloqueado(2)
le.leitorBloqueado(3)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.leitorLendo(3)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.leitorLendo(1)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.escritorEscrevendo(1)
le.leitorBloqueado(1)
le.escritorBloqueado(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(2)
le.escritorBloqueado(2)
# Thread escritora 2 escreveu
le.leitorBloqueado(2)
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.leitorBloqueado(1)
le.leitorBloqueado(1)
le.leitorBloqueado(2)
le.escritorBloqueado(2)
le.escritorSaindo(1)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.leitorBloqueado(2)
le.leitorBloqueado(1)
le.leitorBloqueado(1)
le.escritorSaindo(2)
le.leitorLendo(1)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 1 leu
le.leitorLendo(1)
# O elemento central tem valor 2 e eh primo
# Thread leitora 1 leu
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
le.leitorSaindo(1)
le.leitorSaindo(1)
le.leitorSaindo(2)
le.escritorEscrevendo(3)
le.escritorBloqueado(3)
le.leitorBloqueado(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh primo
# Thread leitora 3 leu
le.escritorBloqueado(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(1)
# O elemento central tem valor 6 e nao eh primo
le.escritorBloqueado(1)
le.escritorBloqueado(1)
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(4)
# O elemento central tem valor 1 e eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.leitorLendo(1)
le.leitorLendo(1)
# O elemento central tem valor 1 e eh primo
le.leitorLendo(2)
# O elemento central tem valor 1 e eh impar
le.escritorBloqueado(1)
# O elemento central tem valor 1 e eh primo
# Thread leitora 2 leu
# Thread leitora 1 leu
le.escritorBloqueado(2)
# Thread leitora e escritora 1 leu
le.leitorLendo(2)
# O elemento central tem valor 1 e eh impar
# Thread leitora e escritora 2 leu
le.leitorSaindo(1)
le.leitorSaindo(1)
le.leitorSaindo(2)
le.leitorSaindo(2)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.leitorLendo(1)
le.escritorBloqueado(1)
# O elemento central tem valor 2 e eh primo
le.escritorBloqueado(1)
# Thread leitora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(3)
# O elemento central tem valor 2 e eh primo
# Thread leitora 3 leu
le.escritorBloqueado(3)
le.leitorLendo(3)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(1)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 1 leu
le.escritorBloqueado(2)
le.escritorBloqueado(2)
le.leitorLendo(2)
# O elemento central tem valor 3 e eh primo
# Thread leitora 2 leu
le.leitorLendo(1)
# O elemento central tem valor 3 e eh primo
# Thread leitora 1 leu
le.escritorBloqueado(1)
le.leitorSaindo(1)
le.leitorSaindo(2)
le.leitorSaindo(1)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorBloqueado(2)
le.escritorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.leitorBloqueado(1)
le.escritorBloqueado(1)
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 2 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.leitorLendo(4)
# O elemento central tem valor 2 e eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
# Thread leitora 2 leu
le.leitorLendo(1)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 1 leu
le.leitorSaindo(2)
le.escritorBloqueado(2)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh par
le.escritorBloqueado(1)
# Thread leitora e escritora 2 leu
le.leitorLendo(1)
# O elemento central tem valor 2 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.leitorSaindo(2)
le.leitorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(3)
# O elemento central tem valor 1 e eh primo
# Thread leitora 3 leu
le.escritorBloqueado(3)
le.escritorBloqueado(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.escritorEscrevendo(1)
le.leitorBloqueado(1)
# Thread escritora 1 escreveu
le.escritorBloqueado(1)
le.escritorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.leitorBloqueado(1)
le.escritorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 2 e eh primo
# Thread leitora 1 leu
le.leitorSaindo(1)
le.leitorLendo(1)
# O elemento central tem valor 2 e eh par
# Thread leitora e escritora 1 leu
le.escritorBloqueado(2)
le.leitorLendo(2)
# O elemento central tem valor 2 e eh primo
le.leitorSaindo(1)
# Thread leitora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorBloqueado(2)
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(3)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 3 leu
le.leitorLendo(3)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.leitorLendo(4)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 4 leu
le.escritorBloqueado(3)
le.leitorSaindo(4)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(1)
# O elemento central tem valor 3 e eh impar
le.leitorLendo(2)
# O elemento central tem valor 3 e eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
# Thread leitora e escritora 1 leu
le.leitorLendo(2)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorBloqueado(2)
le.leitorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(2)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 2 leu
le.escritorBloqueado(2)
le.leitorLendo(1)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 1 leu
le.escritorBloqueado(2)
le.leitorSaindo(1)
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorBloqueado(3)
le.leitorBloqueado(3)
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh primo
# Thread leitora 3 leu
le.escritorBloqueado(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(4)
# O elemento central tem valor 12 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.leitorLendo(2)
# O elemento central tem valor 12 e nao eh primo
# Thread leitora 2 leu
le.escritorBloqueado(2)
le.leitorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 12 e eh par
# Thread leitora e escritora 2 leu
le.escritorBloqueado(2)
le.leitorSaindo(2)
le.leitorLendo(1)
# O elemento central tem valor 12 e eh par
# Thread leitora e escritora 1 leu
le.escritorBloqueado(2)
le.leitorSaindo(1)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(3)
le.leitorLendo(3)
# O elemento central tem valor 4 e nao eh primo
le.escritorBloqueado(3)
# O elemento central tem valor 4 e eh par
# Thread leitora 3 leu
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread escritora 2 escreveu
le.leitorBloqueado(2)
le.escritorBloqueado(2)
le.escritorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.leitorLendo(2)
# O elemento central tem valor 4 e nao eh primo
# Thread leitora 2 leu
le.leitorSaindo(2)
le.leitorLendo(1)
# O elemento central tem valor 4 e eh par
# Thread leitora e escritora 1 leu
le.leitorSaindo(1)
le.escritorEscrevendo(1)
# Thread leitora e escritora 1 escreveu
le.escritorSaindo(1)
le.leitorLendo(4)
# O elemento central tem valor 8 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.leitorLendo(2)
# O elemento central tem valor 8 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.leitorBloqueado(3)
le.escritorBloqueado(3)
le.escritorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.leitorBloqueado(3)
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh primo
# Thread leitora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(4)
# O elemento central tem valor 3 e eh primo
# Thread leitora 4 leu
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorLendo(3)
# O elemento central tem valor 3 e eh primo
le.leitorSaindo(3)
# Thread leitora 3 leu
le.leitorSaindo(4)
le.leitorSaindo(3)
le.leitorLendo(2)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorBloqueado(3)
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 12 e nao eh primo
# Thread leitora 3 leu
le.escritorBloqueado(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(4)
# O elemento central tem valor 3 e eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.leitorLendo(2)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.leitorLendo(3)
# O elemento central tem valor 3 e eh impar
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.leitorLendo(4)
# O elemento central tem valor 6 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
le.leitorLendo(2)
# O elemento central tem valor 6 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.leitorLendo(3)
le.leitorLendo(4)
# O elemento central tem valor 24 e nao eh primo
# Thread leitora 4 leu
le.leitorSaindo(4)
# O elemento central tem valor 24 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.leitorLendo(2)
# O elemento central tem valor 24 e eh par
# Thread leitora e escritora 2 leu
le.leitorSaindo(2)
le.escritorEscrevendo(2)
# Thread leitora e escritora 2 escreveu
le.escritorSaindo(2)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 96 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 192 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
le.leitorLendo(3)
# O elemento central tem valor 384 e eh par
# Thread leitora e escritora 3 leu
le.leitorSaindo(3)
le.escritorEscrevendo(3)
# Thread leitora e escritora 3 escreveu
le.escritorSaindo(3)
