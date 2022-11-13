
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