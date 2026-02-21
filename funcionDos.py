#Funcion que crea lista de N notas 

import random
def crear_lista_notas(numeroNotas):
    notas = []
    for _ in range(numeroNotas):
        nota = random.randint(1,5)
        notas.append(nota)
    return notas