class Fila: 
    
    def __init__(self): 
        self.items = [] 
    
    def is_empty(self): 
        return len(self.items) == 0 
    
    def enqueue(self, item): 
        self.items.append(item) 
    
    def dequeue(self): 
        if self.is_empty(): 
            raise Exception('Fila vazia') 
        return self.items.pop(0) 
    
    def first(self): 
        if self.is_empty(): 
            raise Exception('Fila vazia') 
        return self.items[0] 
    
    def __len__(self): 
        return len(self.items) 

    def compara_filas(self, fila1, fila2):

        if len(fila1) == len(fila2):
            
            filas_iguais=True
            item1=  fila1.dequeue()
            item2=  fila2.dequeue()
                
            if item1 != item2:
                return False

            else:
                fila1.enqueue(item1)
                fila2.enqueue(item2)

        else:
            filas_iguais=False
        
        return filas_iguais

#programa principal

fila1= Fila()
fila1.enqueue('Rafael')
fila1.enqueue('Will')
fila1.enqueue('Macedo')

fila2= Fila()
fila2.enqueue('Rafael')
fila2.enqueue('Will')
fila2.enqueue('Macedo')


resultado= compara_filas (fila1, fila2)
print (fila1)
print (fila2)