'''Considerando uma entrada num que sempre será um número par, escreva a função recursiva soma_pares(num) que devolve (retorna) a soma de todos os números pares de 0 até num.

Sua função será chamada pelo programa base. Você não deve utilizar nenhuma instrução input(). Caso você utilize algum comando input(), um erro será gerado pela plataforma The Huxley.


OBS: neste problema, o número num que será passado por parâmetro para a função será sempre par.

A função deverá retornar (devolver) a soma dos pares de 0 até num. Não utilize a instrução print(), pois isso causará erros na plataforma The Huxley.
'''

def soma_pares(num):

    if num == 0:
        return 0
    else:
        return num + (soma_pares(num-2))

print('Soma Pares:', soma_pares(4))


'''
Escreva a função recursiva exibir_numeros(num, limite) que recebe como parâmetros um número inteiro num e um número inteiro limite e exibe todos os números inteiros de num até limite em ordem crescente.
Sua função será chamada pelo programa base. Você não deve utilizar nenhuma instrução input(). Caso você utilize algum comando input(), um erro será gerado pela plataforma The Huxley.
Sua função deverá exibir (imprimir) nos números inteiros de num até limite. Para isso, utilize instruções print() quando necessário.
Você deve apenas imprimir números. Qualquer outra informação diferente causará erro no The Huxley.
Dica: veja os exemplos de saídas abaixo e confira se a sua função produz (imprime) saídas iguais.
Dica: num e limite podem ser números positivos ou negativos.
'''

def exibir_numeros(num, limite):

    if num == limite:
        print(num)
    else:        
        print(num)
        return (exibir_numeros(num+1,limite))

print('Exibir números:')
exibir_numeros(5,9)

'''
Considerando uma entrada num que poderá ser qualquer valor (par ou ímpar), escreva a função recursiva soma_pares_melhorada(num) que devolve (retorna) a soma de todos os números pares de 0 até num se e somente se num for par, ou de 0 até num-1 se e somente se num for ímpar.

Sua função será chamada pelo programa base. Você não deve utilizar nenhuma instrução input(). Caso você utilize algum comando input(), um erro será gerado pela plataforma The Huxley.

A função deverá retornar (devolver) a soma dos pares. Não utilize a instrução print(), pois isso causará erros na plataforma The Huxley.
'''
def soma_pares_melhorada(num):
    if num % 2 == 0:
        if num == 0:
            return 0
        else:
            return num + (soma_pares_melhorada(num-2))
    else:
        if num == num-1:
            return num-1
        else:
            
            return (soma_pares_melhorada(num-1))

print('Soma pares melhorada:', soma_pares_melhorada(5))