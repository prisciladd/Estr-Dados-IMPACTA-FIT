class No:
    def __init__(self, dado, prox):
        self.dado = dado
        self.prox = prox

# Programa Principal

cabeca = No ("João", None)
ultimo = cabeca 

novo_no = No ("Pedro", None) 
ultimo.prox = novo_no 
ultimo = novo_no 

novo_no = No("Maria",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Bia",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("José",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Priscila",None)
novo_no.prox = cabeca
cabeca = novo_no

novo_no = None 

