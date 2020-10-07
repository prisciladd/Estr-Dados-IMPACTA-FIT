def busca_binaria (lista, x):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio=(inicio+fim) //2
        if lista[meio] == x: #x igual ao meio
            return meio
        elif x > lista[meio]: #x maior que meio
            inicio=meio+1
        else: #x menor que meio
            fim=meio-1
    return -1


nomes=['Brendon', 'Bruno', 'Claudio', 'Fabiola', 'Joao', 'Vitor']
indice= busca_binaria(nomes, 'Claudio')
print('Valor devolvido pela função:', indice)