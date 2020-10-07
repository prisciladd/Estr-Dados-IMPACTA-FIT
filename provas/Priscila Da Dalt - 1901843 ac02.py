import random
import base64
import urllib.request
import ssl


# Coloque o seu nome completo e RA como strings.
NOME_COMPLETO = 'Priscila da Dalt'
RA = '1901843'

"""
ANTES DE COMEÇAR, LEIA ATENTAMENTE AS INSTRUÇÕES:
Nesta atividade você deve ordenar algumas listas numéricas de acordo com o enunciado.
Para ter acesso ao enunciado, complete as variáveis NOME_COMPLETO e RA.
Atenção: caso o seu nome completo e RA esteja diferente do cadastrado no sistema, sua nota será 0 (zero)!
Atenção: você deve entregar ESTE código .py como resposta. Caso entregue em outro formato e caso o seu código não rode, sua nota será 0 (zero)!


Antes de começar, observe os problemas resolvidos nos exemplos abaixo. Eles vão te ajudar a resolver o problema.

Exemplo resolvido 1):
Considere a questão hipotética: Ordene a lista [24, 76, 59, 84, 63] de acordo com o algoritmo de seleção.

Na resposta, você deve fazer o passo a passo do algoritmo de seleção (ou outro algoritmo pedido na questão).
Na primeira linha da resposta, repita a lista do enunciado da questão.
No passo 1 do algoritmo de seleção, você deve procurar o menor elemento e trocá-lo com o elemento na primeira posição da lista.
No passo 2 do algoritmo de seleção, você deve procurar o menor elemento da lista a partir do índice 1 e trocá-lo com o elemento no índice 1.
Os demais passos são análogos. Observe o exemplo resolvido abaixo:

questao1_exemplo = [
[24, 76, 59, 84, 63],    # Na primeira linha da resposta, repita a lista original.
[24, 76, 59, 84, 63],    # A partir desta linha, comece a ordenar a lista (passo 1 do algoritmo de seleção).
[24, 59, 76, 84, 63],    # Passo 2 do algoritmo de seleção.
[24, 59, 63, 84, 76],    # Passo 3 do algoritmo de seleção.
[24, 59, 63, 76, 84]     # Repita o processo até a sua lista estar totalmente ordenada.
]


Exemplo resolvido 2):
Considere a questão hipotética: Ordene a lista [92, 10, 85, 95, 62, 24, 17] de acordo com o método da bolha.

questao2_exemplo = [
[92, 10, 85, 95, 62, 24, 17],     # Copie a lista original aqui.
[10, 85, 92, 62, 24, 17, 95],     # "Borbulhe" o maior elemento até o fim da lista
[10, 85, 62, 24, 17, 92, 95],     # "Borbulhe" o segundo maior elemento até a penúltima posição da lista
[10, 62, 24, 17, 85, 92, 95],     # os próximos passos são análogos...
[10, 24, 17, 62, 85, 92, 95],
[10, 17, 24, 62, 85, 92, 95]      # ... até que a lista esteja ordenada!
]


Exemplo resolvido 3):
Considere a questão hipotética: ordende a lista [7, 70, 92, 4, 30, 58, 80, 26, 22] de acordo com o método de inserção.

questao3_exemplo = [
[7, 70, 92, 4, 30, 58, 80, 26, 22],   # Copie a lista original aqui.
[7, 70, 92, 4, 30, 58, 80, 26, 22],   # Considere que o elemento L[0] está ordenado. Encaixe o elemento L[1] na posição correta na sublista L[0:2].
[7, 70, 92, 4, 30, 58, 80, 26, 22],   # Considere a sublista L[0:2] está ordenada. Encaixe o elemento L[2] na posição correta  na sublista L[0:3].
[4, 7, 70, 92, 30, 58, 80, 26, 22],   # Considere que a sublista L[0:3] está ordenada. Encaixe o elemento L[3] na posição correta  na sublista L[0:4].
[4, 7, 30, 70, 92, 58, 80, 26, 22],   # os próximos passos são análogos...
[4, 7, 30, 58, 70, 92, 80, 26, 22],
[4, 7, 30, 58, 70, 80, 92, 26, 22],
[4, 7, 26, 30, 58, 70, 80, 92, 22],
[4, 7, 22, 26, 30, 58, 70, 80, 92]    # ... até que a lista esteja ordenada!
]
"""

# Coloque aqui as respostas da QUESTÃO 1
questao_1 = [
[61, 78, 42, 64, 1, 42, 50],
[1, 78, 42, 64, 61, 42, 50],
[1, 42, 78, 64, 61, 42, 50],
[1, 42, 42, 64, 61, 78, 50],
[1, 42, 42, 50, 64, 78, 61],
[1, 42, 42, 50, 61, 78, 64],
[1, 42, 42, 50, 61, 64, 78],
[1, 42, 42, 50, 61, 64, 78],
]

# Coloque aqui as respostas da QUESTÃO 2
questao_2 = [
[68, 24, 47, 84, 53, 84, 58, 81],
[24, 47, 68, 53, 84, 58, 81, 84],
[24, 47, 53, 68, 58, 81, 84, 84],
[24, 47, 53, 58, 68, 81, 84, 84],
]

# Coloque aqui as respostas da QUESTÃO 3
questao_3 = [
[13, 71, 94, 36, 8, 65, 65, 0, 53],
[13, 71, 94, 36, 8, 65, 65, 0, 53],
[13, 71, 94, 36, 8, 65, 65, 0, 53], 
[13, 36, 71, 94, 8, 65, 65, 0, 53], 
[8, 13, 36, 71, 94, 65, 65, 0, 53], 
[8, 13, 36, 65, 71, 94, 65, 0, 53],
[8, 13, 36, 65, 65, 71, 94, 0, 53],
[0, 8, 13, 36, 65, 65, 71, 94, 53],
[0, 8, 13, 36, 53, 65, 65, 71, 94], 
]


















# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #
"""
		NÃO EDITE O CÓDIGO A PARTIR DESTE PONTO
"""
# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #

def testa_ordenada(lista):
	for i in range(1, len(lista)):
		if lista[i-1] > lista[i]:
			return False
	return True

def mistura_lista(lista):
	for i in range(1, len(lista), 3):
		lista[i-1], lista[i] = lista[i], lista[i-1]

def lista_aleatoria(seed, tamanho, testaOrdenada=True):
	random.seed(seed)
	lista = []
	for i in range(tamanho):
		lista.append(random.randint(0, 99))
	if testa_ordenada(lista) and testaOrdenada:
		mistura_lista(lista)
	return lista

def calcula_semente(texto):
	s = 0
	for i in range(len(texto)-1, -1, -1):
		s += ord(texto[i])**(i+1)
	seed = s % 433494437
	return seed

def obter_listas_aluno(nome, tamanhos_listas=[7, 8, 9]):
	listas = []
	seed = calcula_semente(nome)
	for tamanho in tamanhos_listas:
		lista = lista_aleatoria(seed+tamanho+2, tamanho)
		listas.append(lista)
	return listas

def obter_questao(questao):
	if questao.upper() == 'Q1':
		return 'algoritmo de seleção'
	elif questao.upper() == 'Q2':
		return  'algoritmo da bolha'
	elif questao.upper() == 'Q3':
		return 'algoritmo de inserção'

def main(questoes):
	if NOME_COMPLETO.strip().upper() and str(RA).strip().upper():
		print('\nAluno (RA): {0} ({1})'.format(NOME_COMPLETO, RA))
		listas = obter_listas_aluno(NOME_COMPLETO.upper() + str(RA))
		print('\nListas que você deve ordenar:')
		for i in range(1, len(listas)+1):
			alg = obter_questao('q{0}'.format(i))
			print('QUESTÃO {0}: {1}, usando o {2}.'.format(i, listas[i-1], alg))
		print('\n======== NOTAS PARCIAIS ===============')
		try:
			b64listas = base64.b64encode(str(listas).encode('ascii')).decode('ascii')
			b64questoes = base64.b64encode(str(questoes).encode('ascii')).decode('ascii')
			req = response = urllib.request.urlopen('http://www.ime.usp.br/~rwill/tarefa/estdados_ac2/index.php?lists={0}&answers={1}&classid={2}'.format(b64listas, b64questoes, 'ads3csi3b021622'), context=ssl._create_unverified_context())
			str_notas = req.read().decode('utf-8')
			notas = eval(str_notas)
			media = 0.0
			for i in range(1, len(notas)+1):
				media += notas[i-1]/len(notas)
				print('Nota da questão {0}: {1:5.2f}'.format(i, notas[i-1]))
			print('Nota final: {0:5.2f}'.format(media))
			return (notas, media)
		except:
			print('Erro ao executar o corretor automático.')
			return -1
	else:
		print('Para iniciar a atividade você deve preencher o seu nome completo na variável NOME_COMPLETO e o seu número de matrícula na variável RA.')
		print('\nATENÇÃO: A atividade é vinculada ao seu nome completo e ao seu RA. Preste muita atenção ao preencher esses campos para não ficar com nota zero.')
	print('')
if __name__ == '__main__':
	main([questao_1, questao_2, questao_3])
	input(' --- Pressione <ENTER> para encerrar ---')

