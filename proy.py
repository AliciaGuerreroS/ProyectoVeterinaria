
"""
Veterinaria necesita revisar y registrar datos de una mascota

Datos de una mascota:

Nombre
Fecha de nacimiento
Raza
Nombre de dueño(a)
DNI del dueño(a)
Por el momento no se tomará en cuenta datos relacionados a su histórico de visitas ni peso o talla.

En una veterinaria se requiere una pequeña interfaz por línea de comandos que permita:

Opción 1: Cargar un archivo csv con datos de 5 mascotas. Tras una persona seleccionar esta opción, debe el sistema indicar un mensaje "Se cargaron los datos de 5 mascotas".
Opción 2: Mostrar datos de mascotas cargadas en el sistema.
Opción 3: Agregar mascota. En esta opción el sistema solicita los datos de la mascota para su registro.
Opción 4: Buscar mascota. Al seleccionar esta opción, el sistema indicar subopciones de búsqueda como: nombre mascota, dueño, raza, edad o DNI. Acorde a la opción y valor ingresado se debe mostrar las mascotas que cumplen dichos criterios.
Opción 5: Ordenar mascota. Al seleccionar esta opción, el sistema indicar subopciones de ordenamiento como: nombre mascota, dueño, raza, edad o DNI. Acorde a la opción y valor ingresado se debe mostrar las mascotas que cumplen dichos criterios.
Opción 6: Guardar mascotas en archivo de disco duro (.txt o csv)
Se solicita escribir un programa en Python que permita realizar las gestiones descritas en las opciones líneas arriba. Para ello, se debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python. En caso deseen utilizar otros tópicos de Python no hay restricciones.

Nota: mostrar datos de mascota involucra: nombre, edad, raza, dueño y DNI del dueño.

"""

lista_opciones = [1, 2, 3, 4, 5, 6]

print("Bienvenidos a la veterinaria")
print("¿Que accion desea realizar?")
print("""Opción 1: Cargar un archivo csv con datos de mascotas
Opción 2: Mostrar datos de mascotas cargadas en el sistema
Opción 3: Agregar mascota al registro
Opción 4: Buscar mascota 
Opción 5: Ordenar lista de mascotas
Opción 6: Guardar mascotas en archivo de disco duro (.txt o csv)""")

while True:
    while True:
        try:

            opcion = int(input("Ingresa el numero de la opcion: "))
            #colocar un try en la linea anterior para los errores de typo de datos ingresados y que se vuelva a ingresar
        except: 
            print("Por favor ingresa un numero valido")

        else: 
            break
        
    if opcion in lista_opciones:
        print(f"Opcion {opcion} ")

        if opcion == 1:
            print("Opcion 1")
            break

        elif opcion == 2:
            print("Opcion 2")
            break

        elif opcion == 3:
            print("Opcion 3")
            break

        elif opcion == 4:
            print("Opcion 4")
            break

        elif opcion == 5:
            print("Opcion 5")
            break

        else:
            print("Opcion 6")
            break

    else:
        print("ingrese el numero de la opcion entre 1 y 6 ")

"""""
if opcion in lista_opciones:
    print(f"Opcion {opcion}")   

else:
    print("ingrese el numero de la opcion entre 1 y 6 ")

Este podria ser el resumen de las lineas 42 en adelante
"""""

print("Por favor ingrese los datos de la mascota: ")
class Mascota:
    def __init__(self, nombre, fecha_nacimiento, raza, nombre_dueño, DNI_dueño):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.raza = raza
        self.nombre_dueño = nombre_dueño
        self.DNI_dueño = DNI_dueño

__dict__ = []

nombre = input("Nombre: ")
fecha_nacimiento = input("Fecha de nacimiento: ")
raza = input("Raza: ")
nombre_dueño = input("Nombre del dueño: ")
DNI_dueño = input("DNI del dueño: ")

lista_datos = []
mascota1 = Mascota(nombre, fecha_nacimiento, raza, nombre_dueño, DNI_dueño )
__dict__.append(mascota1) 
for i in __dict__:
    print(i)


print(mascota1.nombre)
print(mascota1.fecha_nacimiento)
print(mascota1.raza)
print(mascota1.nombre_dueño)
print(mascota1.DNI_dueño)
>>>>>>> origin
