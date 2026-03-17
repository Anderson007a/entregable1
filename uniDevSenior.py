"""
Una universidad quiere desarrollar un pequeño programa en Python que permita registrar estudiantes y evaluar su estado académico de forma simple desde la terminal.

Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de estudiantes, calcular su promedio y mostrar su estado académico.

Requisitos del programa

El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final

Reglas del sistema

Para cada estudiante se debe ingresar:

Nombre

Edad

Nota 1

Nota 2

Nota 3

El programa debe calcular:

promedio = (nota1 + nota2 + nota3) / 3

Y determinar el estado académico:

Promedio	Estado
>= 4.0	Aprobado
>= 3.0 y < 4.0	En recuperación
< 3.0	Reprobado
Estructura obligatoria del programa

El programa debe tener al menos estas funciones:

1️⃣ Función para registrar estudiante
def registrar_estudiante():

Debe pedir:

nombre

edad

3 notas

Debe retornar los datos.

2️⃣ Función para calcular promedio
def calcular_promedio(n1, n2, n3):

Debe retornar el promedio.

3️⃣ Función para determinar estado
def evaluar_estado(promedio):

Debe retornar:

"Aprobado"

"En recuperación"

"Reprobado"

4️⃣ Menú principal con bucle

El programa debe mostrar un menú como este:

1. Registrar estudiante
2. Salir

Debe usar un while para permitir registrar varios estudiantes.

Ejemplo de salida esperada
===== SISTEMA DE ESTUDIANTES =====

Ingrese el nombre del estudiante: Ana
Ingrese la edad: 20
Ingrese nota 1: 4.5
Ingrese nota 2: 3.8
Ingrese nota 3: 4.2

Promedio del estudiante: 4.17
Estado académico: Aprobado
Validaciones mínimas

El programa debe validar:

Que las notas estén entre 0 y 5

Que la edad sea mayor que 0

Si los datos no son válidos, debe pedirlos nuevamente.

Parte final (obligatoria)

Al terminar el programa debe mostrar:

Total de estudiantes registrados: X
Promedio general del grupo: X

"""



listado = """

==== SISTEMA DE GESTION DE ESTUDIANTES ====

1. Registrar estudiante
2. Mostrar todos los estudiantes
3. Salir
"""

#1. Creamos la lista vacía para almacenar los datos

registroEstudiante = []
promEst = []

while True: 
    opcion = input(f" {listado} Selecciona una opción: ")       
    
    if opcion == "1":
        print("\n=== Registro De Estudiante ===")
        nuevo_registro = input("Ingrese el nombre del estudiante: ")
        
        # Pedimos el número y lo convertimos a entero o flotante
        n1 = float(input("Ingrese La Nota 1: "))
        n2 = float(input("Ingrese La Nota 2: "))
        n3 = float(input("Ingrese La Nota 3: "))
        prom = (n1 + n2 + n3)/ 3 
        
        registroEstudiante.append(nuevo_registro)
        promEst.append(prom)
        
        # .append() agrega el elemento al final de la lista
        print(f"¡Registro {nuevo_registro} guardado con éxito!")

    elif opcion == "2":
        if len(registroEstudiante) == 0:
            print("No hay nombres en la lista aún.")
        else:
            print(f"\nHay {len (registroEstudiante)} personas en la lista:")
            # Usamos enumerate para que salgan numerados (1. Jose, 2. Ana...)
            for i, n in enumerate(registroEstudiante, 1):
                promedio_actual = promEst[i-1]
                print(f"{i}. Estudiante: {n} Promedio: {promedio_actual: .2f}")

    elif opcion == "3":
        print("Saliendo del programa, hasta pronto")
        break
    
    else:
        print("Opción no válida, intenta de nuevo.")