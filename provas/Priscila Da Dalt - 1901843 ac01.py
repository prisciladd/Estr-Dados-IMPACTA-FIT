import unittest
import hashlib

"""
Leia atentamente as instruções:
	- Renomeie o arquivo com o padrão: "Seu Nome Completo - Seu RA", com a extensão .py.
	- O arquivo deve estar no formato de código/arquivo texto. Arquivos que não rodam terão nota 0 (zero)!
	- Coloque o seu nome completo como string na variável NOME_COMPLETO (abaixo).
	- Coloque o seu RA como string na variável RA_ALUNO (abaixo).
	- IMPORTANTE: Casos de plágio terão a nota de TODOS OS ENVOLVIDOS cortada pela metade.
	- IMPORTANTE: Casos reincidentes de plágio receberão nota 0 (zero)!!!
"""

# OBRIGATÓRIO: coloque o seu nome COMPLETO e RA como string nas variáveis abaixo:
NOME_COMPLETO = 'Priscila Da Dalt'
RA_ALUNO = '1901843'


"""
Questão 1: Dada uma lista, escreva a função reposiciona_maior(lista) que percorre toda a lista,
encontra o maior elemento dessa lista e o seu respectivo índice (vamos chamá-lo de i_maior).
Ao fim, faça a troca entre o último elemento da lista (isto é, o elemento lista[len(lista)-1])
pelo elemento em lista[i_maior].

Restrições: esta tarefa deve ser realizada sem o uso de funções auxiliares. Está proibido
o uso das funções/métodos: list(), min(), max(), sum(), list.index(), list.reverse(),
list.sort().

Entrada:
	- lista: parâmetro que contém uma lista

Saída:
	- a função deve retornar (devolver) a lista após o fim do processamento. Você não precisa criar
uma nova lista vazia. Basta utilizar a própria lista enviada por parâmetro.

Exemplos de entrada e saída:
	Exemplo 1:
		Entrada: 	[95, 76, 65, 88, 10]
		Saída: 		[10, 76, 65, 88, 95]

	Exemplo 2:
		Entrada: 	[90, 69, 15, 16, 5, 70]
		Saída: 		[70, 69, 15, 16, 5, 90]
"""
def reposiciona_maior(lista):
	maior=lista[0]
	for i in lista:
		i_maior=i
        if i > maior:
            maior=i
            i_maior=lista[i]
        
        lista[0]=lista[len(lista)-1]
        
        lista[len(lista)-1]=maior
	# Você não precisa chamar a função, pois o código de teste faz isso para você.
	return lista # A função deve devolver a lista ao final da execução.










# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #
"""
		>>> NÃO EDITE O CÓDIGO A PARTIR DESTE PONTO ATÉ O FINAL <<<
"""
# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #
class RestrictedList(list):

	def __init__(self, sequence):
		for item in sequence:
			self.append(item)

	def reverse(self):
		raise AttributeError('Proibido o uso do método reverse()')

	def sort(self, reverse=False):
		raise AttributeError('Proibido o uso do método sort()')

	def index(self, value):
		raise AttributeError('Proibido o uso do método index()')

def min(x):
	raise NameError('Proibido o uso da função min()')

def max(x):
	raise NameError('Proibido o uso da função max()')

def sum(x):
	raise NameError('Proibido o uso da função sum()')

def list(x):
	raise NameError('Proibido o uso da função list()')

class TesteAtividade01(unittest.TestCase):
	def test_01(self):
		resp = reposiciona_maior(RestrictedList([73]))
		self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(), '3beb68991a935395556e08b5ff500c7a27cf70720abf88a8b97878bf')
	def test_02(self):
		resp = reposiciona_maior(RestrictedList([22, 50]))
		self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(), 'cdc41071eb60a6e1d84a22c13f2e8506f4fd9ed79e04382fd0c3d9f7')
	def test_03(self):
		resp = reposiciona_maior(RestrictedList([53, 76, 65]))
		self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(), '296913b553f4a4ef307ed9733413e11cfedd20023c61cdec0ec14634')
	def test_04(self):
		resp = reposiciona_maior(RestrictedList([17, 58, 54, 37]))
		self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(), 'cfb3ca69b11e39f63fa6c65dd1f10bffb6b200c3f5b667660f36d819')
	def test_05(self):
		resp = reposiciona_maior(RestrictedList([71, 65, 95, 2, 20]))
		self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(), '09d3b2c0ef0c205fd8ebc41978f2ad8a0e6cf738e49c2b9e17ca17b8')
	def test_06(self):
		resp = reposiciona_maior(RestrictedList([62, 81, 27, 57, 21, 83, 24, 94, 94, 80, 57, 61, 34, 56, 83, 89, 17, 72, 40, 87, 45, 41, 85, 44, 13, 54, 24, 52, 34, 32, 87, 55, 50, 3, 91, 48, 89, 52, 93, 47, 74, 96, 96, 66, 20, 73, 82, 92, 4, 35]))
		self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(), 'f7f4e71e814d683b2c38b5e341d5d5525c7a2dc264dcfd24f0a44705')

if __name__ == '__main__':
	input(' ATENÇÃO: casos de plágio terão a nota de TODOS OS ENVOLVIDOS cortada pela metade. Casos reincidentes receberão nota 0 (zero). \n\t >>> PRESSIONE ENTER PARA CONTINUAR <<<')
	unittest.main()



