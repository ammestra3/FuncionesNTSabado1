def crear_lista_estudiantes(numeroEstudiantes):
    estudiantes = []
    for _ in range(numeroEstudiantes):
        estudiante = {}
        estudiante["id"]= input("Ingrese el id: ")
        estudiante["nombre"]= input("Ingrese el nombre: ")
        estudiante["documento"]= input("Ingrese el documento: ")
        estudiante["semestre"]= input("Ingrese el semestre: ")
        estudiantes.append(estudiante)
    return estudiantes

crear_lista_estudiantes(5)