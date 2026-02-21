#crear una lista de 500 notas (1,5)
#mock 

import random
notas=[]
for i in range(5):
    
    nota=random.randint(1,5)
   
   #aprender a llenar una lista con un ciclo for 

    notas.append(nota)

#manipulando listas con python

notas.insert(1,80)
notas.remove(80)
notas.pop(0) #elimina el primer elemento de la lista
notas.sort(reverse=True) #ordena la lista de menor a mayor
notas.clear() #elimina todos los elementos de la lista
print(notas)