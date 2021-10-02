import checkProdCons
checker = checkProdCons.PRODCONS()
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 1 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 8 retirado 
# Elemento 8 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 7 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 3 retirado 
# Elemento 5 inserido 
# Elemento 1 retirado 
checker.insertInBuffer(3, 5)
# Elemento 3 inserido 
# Elemento 5 retirado 
# Elemento 8 retirado 
checker.insertInBuffer(1, 3)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 4 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 7 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 2 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 8 retirado 
# Elemento 5 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 2 retirado 
# Elemento 7 retirado 
# Elemento 8 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 1 retirado 
# Elemento 6 retirado 
# Elemento 4 inserido 
# Elemento 5 retirado 
checker.insertInBuffer(3, 4)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 6 retirado 
# Elemento 6 retirado 
# Elemento 6 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 4 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 8 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 3 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 8 retirado 
# Elemento 3 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 3 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 6 retirado 
# Elemento 6 retirado 
# Elemento 2 retirado 
# Elemento 8 retirado 
# Elemento 6 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 4 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 6 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 2 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 7 retirado 
# Elemento 2 inserido 
# Elemento 3 retirado 
checker.insertInBuffer(2, 2)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 2 retirado 
# Elemento 6 retirado 
# Elemento 6 retirado 
# Elemento 1 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 3 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 6 retirado 
# Elemento 8 retirado 
# Elemento 2 retirado 
# Elemento 3 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 4 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 1 retirado 
# Elemento 5 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 8 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 8 inserido 
# Elemento 3 retirado 
checker.insertInBuffer(4, 8)
# Elemento 1 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 8 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 6 inserido 
# Elemento 3 retirado 
checker.insertInBuffer(4, 6)
# Elemento 6 retirado 
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 6 retirado 
# Elemento 1 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 5 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 8 retirado 
# Elemento 3 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 3 inserido 
# Elemento 7 retirado 
checker.insertInBuffer(1, 3)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 2 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 1 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 1 retirado 
# Elemento 5 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 7 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 4 retirado 
# Elemento 8 retirado 
# Elemento 4 inserido 
# Elemento 4 retirado 
checker.insertInBuffer(3, 4)
# Elemento 4 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 3 retirado 
# Elemento 6 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 7 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 6 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 3 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 2 retirado 
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 2 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 8 retirado 
# Elemento 2 retirado 
# Elemento 3 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 4 retirado 
# Elemento 7 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 1 retirado 
# Elemento 8 retirado 
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 2 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 8 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 7 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 2 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 7 retirado 
# Elemento 1 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 5 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 8 retirado 
# Elemento 4 retirado 
# Elemento 1 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 8 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 7 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 5 inserido 
# Elemento 7 retirado 
checker.insertInBuffer(1, 5)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 4 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 6 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 7 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 1 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 1 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 3 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 7 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 2 retirado 
# Elemento 4 retirado 
# Elemento 2 retirado 
# Elemento 4 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 1 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 8 retirado 
# Elemento 6 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 1 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 7 retirado 
# Elemento 7 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 6 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 6 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 2 retirado 
# Elemento 7 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 2 retirado 
# Elemento 6 retirado 
# Elemento 7 retirado 
# Elemento 8 retirado 
# Elemento 5 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 5 inserido 
# Elemento 3 retirado 
checker.insertInBuffer(4, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 8 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 8 retirado 
# Elemento 4 retirado 
# Elemento 7 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 5 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 3 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 6 retirado 
# Elemento 8 inserido 
# Elemento 3 retirado 
checker.insertInBuffer(4, 8)
# Elemento 1 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 8 retirado 
# Elemento 3 retirado 
# Elemento 2 retirado 
# Elemento 4 retirado 
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 4 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 8 retirado 
# Elemento 2 retirado 
# Elemento 6 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 2 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 6 retirado 
# Elemento 3 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 8 inserido 
checker.insertInBuffer(4, 8)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 8 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 6 retirado 
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 4 retirado 
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 1 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 2 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 4 retirado 
# Elemento 1 retirado 
# Elemento 7 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 6 inserido 
checker.insertInBuffer(3, 6)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 6 retirado 
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 3 retirado 
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 3 inserido 
checker.insertInBuffer(3, 3)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Elemento 3 inserido 
checker.insertInBuffer(2, 3)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 4 retirado 
# Elemento 3 retirado 
# Elemento 3 retirado 
# Elemento 5 retirado 
# Elemento 7 inserido 
# Elemento 3 retirado 
checker.insertInBuffer(3, 7)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 7 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 7 retirado 
# Elemento 2 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 1 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 4 inserido 
checker.insertInBuffer(4, 4)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 2 retirado 
# Elemento 5 retirado 
# Elemento 4 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(1, 5)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 5 retirado 
# Elemento 5 retirado 
# Elemento 3 retirado 
# Elemento 7 retirado 
# Elemento 5 retirado 
# Elemento 4 inserido 
checker.insertInBuffer(2, 4)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 3 inserido 
checker.insertInBuffer(1, 3)
# Elemento 2 inserido 
checker.insertInBuffer(2, 2)
# Produtora 2 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(2)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 4 retirado 
# Elemento 5 retirado 
# Elemento 7 retirado 
# Elemento 3 retirado 
# Elemento 2 retirado 
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Elemento 4 inserido 
checker.insertInBuffer(1, 4)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 5 inserido 
checker.insertInBuffer(4, 5)
# Produtora 4 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(4)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 6 retirado 
# Elemento 7 retirado 
# Elemento 4 retirado 
# Elemento 6 retirado 
# Elemento 5 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 2 inserido 
checker.insertInBuffer(1, 2)
# Elemento 7 inserido 
checker.insertInBuffer(3, 7)
# Produtora 3 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(3)
# Consumidora 6 vai consumir o buffer 
checker.readBuffer(6)
# Elemento 5 retirado 
# Elemento 1 retirado 
# Elemento 5 retirado 
# Elemento 2 retirado 
# Elemento 7 retirado 
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 6 inserido 
checker.insertInBuffer(2, 6)
# Elemento 7 inserido 
checker.insertInBuffer(4, 7)
# Elemento 5 inserido 
checker.insertInBuffer(3, 5)
# Elemento 1 inserido 
checker.insertInBuffer(1, 1)
# Produtora 1 sinalizou que o buffer esta cheio 
checker.sinalizeFullBuffer(1)
# Consumidora 5 vai consumir o buffer 
checker.readBuffer(5)
# Elemento 7 retirado 
# Elemento 6 retirado 
# Elemento 7 retirado 
# Elemento 5 retirado 
# Elemento 1 retirado 
# Elemento 5 inserido 
checker.insertInBuffer(2, 5)
# Elemento 6 inserido 
checker.insertInBuffer(4, 6)
# Elemento 4 inserido 
checker.insertInBuffer(3, 4)
# Elemento 1 inserido 