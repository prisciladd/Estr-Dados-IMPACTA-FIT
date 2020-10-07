class No:
    def __init__(self, dado, prox):
        self.dado = dado
        self.prox = prox

# Programa Principal

cabeca = No (3, None)
ultimo = cabeca #como não tem mais nenhum o ultimo é o primeiro

novo_no = No (5, None) #acrescenta 10 na lista
ultimo.prox = novo_no #aponta para o nó 10
ultimo = novo_no #aponta para o nó 10 
#agora objeto 3 está encadeado com objeto 10

novo_no = No(8,None)
ultimo.prox = novo_no
ultimo = novo_no

#inserir na frente da lista

novo_no = No(2,None)
novo_no.prox = cabeca
cabeca = novo_no

novo_no = None #finaliza lista

#percorrer lista encadeada

def percorre_lista_enc(cabeca):
    no_atual = cabeca
    while no_atual != None:
        print(no_atual.dado)
        no_atual = no_atual.prox

percorre_lista_enc(cabeca)
