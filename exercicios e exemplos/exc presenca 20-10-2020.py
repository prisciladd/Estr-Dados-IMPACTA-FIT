def hash(palavra, tamanho_tabela):
    soma = 0
    for pos in range(len(palavra)):
        soma = soma + ord(palavra[pos])
    return soma % tamanho_tabela

print('impacta', hash('impacta',23))
print('faculdade', hash('faculdade',23))
print('atividade', hash('atividade',23))
print('gato', hash('gato',23))

lista=[None]*23
lista[22]='impacta'
lista[1]='faculdade'
lista[19]='atividade'
print('Tem gato na lista?', lista[13]== 'gato') #procura se existe gato na lista

print(lista)