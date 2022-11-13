 #Hola
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

import csv
from csv import writer
from datetime import date
import pandas as pd


lista_opciones = [1, 2, 3, 4, 5, 6]
#Lista de 

Lista_mascotas_cargadas = []
fila= []
mascotas = []
respuesta = ["si", "no"]


class Mascota:
    def __init__(self, nombre, fecha_nacimiento, raza, nombre_dueño, DNI_dueño):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.raza = raza
        self.nombre_dueño = nombre_dueño
        self.DNI_dueño = DNI_dueño


    def agregar_mascota(self):

        texto1 = f"Nombre: {self.nombre} "
        texto2 = f"Fecha de nacimiento: {self.fecha_nacimiento}"
        texto3 = f"Raza: {self.raza}"
        texto4 = f"Nombre del dueño: {self.nombre_dueño}"
        Texto5 = f"DNI del dueño: {self.DNI_dueño}"
        return mascotas.append([texto1, texto2, texto3, texto4, Texto5])


class Archivo:
    def __init__(self, doc) -> None:
        self.doc= doc

    def cargar_archivo(self):
        with open("MASCOTAS.csv", encoding= 'utf-8') as f:
            self.doc = csv.reader(f)
            print(self.doc)
            for linea in self.doc:
                #print(f"Se cargaron los datos de 5 mascotas")
                print(f"Se cargaronlos datos de: {len(list(self.doc))} Mascotas")

    def mostrar_datos(self, doc):
         with open("MASCOTAS.csv", encoding= 'utf-8') as f:
            self.doc = csv.reader(f)
            #print(self.doc)            
            df=pd.DataFrame(self.doc)
            print(df)


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

            opcion = int(input("Ingresa el numero de la opcion a ejecutar: "))
            #colocar un try en la linea anterior para los errores de typo de datos ingresados y que se vuelva a ingresar
        except: 
            print("Por favor ingresa un numero valido")

        else: 
            break
        
    if opcion in lista_opciones:
        print(f"Opcion {opcion} ")

        if opcion == 1:
            print("Ejecutando Opcion 1")
            break


        elif opcion == 2:
            print("Ejecutando Opcion 2")
            break

        elif opcion == 3:
            print("Ejecutando Opcion 3 ")
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
        print("ingrese el numero de la opcion entre 1 y 6 ")
