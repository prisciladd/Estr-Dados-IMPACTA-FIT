lista = [10,20,5,3,48]
maior = lista[0]
i_maior = 0
for i in range (len(lista)): #i varia do indice 0 até o indice len (lista)-1
    if lista[i] > maior:
        maior = lista[i]
        i_maior = i 

aux = lista[len(lista)-1]
lista[len(lista)-1] = lista[i_maior]
lista[i_maior] = aux

#troca de valor de variável, exemplo de baldes:
# balde 1 com água
# balde 2 com alcool
# como trocar um liquido de balde?
# usar balde 03 vazio 