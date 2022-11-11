
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


opcion = int(input("Ingresa el numero de la opcion: "))

for i in lista_opciones: #en realidad el for no deberia de ir 
    if opcion == i and i == 1:
        print("Opcion 1")

    elif opcion == i and i == 2:
        print("Opcion 2")

    elif opcion == i and i == 3:
        print("Opcion 3") 

    elif opcion == i and i == 4:
        print("Opcion 4")

    elif opcion == i and i == 5:
        print("Opcion 5")

    elif opcion == i and i == 6:
        print("Opcion 6")    

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

nombre = input("Nombre: ")
fecha_de_nacimiento = input("Fecha de nacimiento: ")
raza = input("Raza: ")
nombre_dueño = input("Nombre del dueño: ")
DNI_dueño = input("DNI del dueño: ")


print ("cambio")