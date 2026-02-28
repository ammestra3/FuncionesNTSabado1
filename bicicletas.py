from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista_notas
from funcionTres import calcular_promedio_notas
from funcionCuatro import evaluar_bicicleta

#paso 1: crear la lista de estudiantes
equipoUno=crear_lista_estudiantes(4)

#paso 2: evaluar los componenentes EF,ES,P de la bicileta
notasEficiencia=crear_lista_notas(50)
notasEstabilidad=crear_lista_notas(50)
notasParecido=crear_lista_notas(50)

#Paso 3: calcular la nota promedio de cada componente

eficiencia=calcular_promedio_notas(notasEficiencia)
estabilidad=calcular_promedio_notas(notasEstabilidad)
parecido= calcular_promedio_notas(notasParecido)

#Paso 4: evaluar la bicicleta
evaluacionFinal= evaluar_bicicleta(eficiencia,estabilidad,parecido)

#paso 5: imprimir el resultado de la evaluación

print(f"El resultado del equipoes: {evaluacionFinal}")