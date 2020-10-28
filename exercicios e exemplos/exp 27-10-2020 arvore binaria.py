class ArvoreBinBusca:
    def __init__(self):
        self.arvore = []
        self.qtd_nos = 1

    def inserir(self, item):
        if len(self.arvore) == 0: # se a  ́arvore est ́a vazia, insira na raiz
            self.arvore = [item, [], []]
        else:
            arv = self.arvore
            while True:
                if item == arv[0]: # encontrou o item, ent~ao sai do m ́etodo sem inserir
                    return False
                elif item < arv[0]: # se item < s[0], investigue a sub ́arvore esquerda
                    if len(arv[1]) == 0: # se a sub ́arvore esquerda est ́a vazia, insira
                        arv[1] = [item, [], []]
                        return True
                    else:
                        arv = arv[1] # investigue a sub ́arvore esquerda na pr ́oxima itera ̧c~ao
                elif item > arv[0]: # se item < s[0], investigue a sub ́arvore direita
                    if len(arv[2]) == 0: # se a sub ́arvore direita est ́a vazia, insira
                        arv[2] = [item, [], []]
                        return True
                    else:
                        arv = arv[2]

    def buscar(self, item):
        arv = self.arvore
        while len(arv) > 0: # enquanto a sub ́arvore n~ao for uma lista vazia, fa ̧ca
            if item == arv[0]: # se o item  ́e igual ao n ́o raiz da sub ́arvore, encontramos!
                return True
            elif item < arv[0]: # se o item  ́e menor que a raiz da sub ́arvore, v ́a para a sub ́arvore da esquerda
                arv = arv[1]
            elif item > arv[0]: # se o item  ́e maior que a raiz da sub ́arvore, v ́a para a sub ́arvore da direita
                arv = arv[2]
        return False