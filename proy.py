
import csv
from csv import writer
from datetime import date
import pandas as pd


lista_opciones = [1, 2, 3, 4, 5, 6]

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
            #print(self.doc)
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

        elif opcion == 2:
            print("Ejecutando Opcion 2: MOSTRAR DATOS")


        elif opcion == 3:
            print("Ejecutando Opcion 3 ")
            

        elif opcion == 4:
            print("Ejecutando Opcion 4")
            

        elif opcion == 5:
            print("Ejecutando Opcion 5")
            class Archivo:
                def __init__(self, doc) -> None:
                    self.doc= doc

                def cargar_archivo(self):
                    with open("MASCOTAS.csv", encoding= 'utf-8') as f:
                        self.doc = csv.reader(f)
                        print(f"Se cargaron los datos de 5 mascotas")


                def mostrar_datos(self, doc):
                    with open("MASCOTAS.csv", encoding= 'utf-8') as f:
                        self.doc = csv.reader(f)
                        #print(self.doc)
                        import pandas as pd
                        df=pd.DataFrame(self.doc)
                        print(df)

                        """for linea in self.doc:
                            print(linea)"""

                def ordenar_datos(self,doc):
                    with open("MASCOTAS.csv", encoding= 'utf-8') as f:
                        self.doc = csv.reader(f)
                        import pandas as pd
                        df=pd.DataFrame(self.doc)
                        filtrado=df.loc[1:,[0,1,2,3,4]]
                        #lista_subopciones=[0,1,2,3]
                        nombre_subopciones=['nombre de mascota','raza', 'dueño' , 'DNI']
                        print("OPCION 5: Ordenar datos")
                        print("Se puede ordenar de acuerdo a los siguientes campos:")
                        print("1) Ordenar por nombre de mascota")
                        #print("2) Ordenar por Fecha de Nacimiento")
                        print("2) Ordenar por Raza")
                        print("3) Ordenar por Dueño")
                        print("4) Ordenar por DNI dueño")

                        while True:
                            opcion = int(input("Ingresa el numero de la subopcion: "))

                            if opcion == 1:
                                print("Se ordenara de acuerdo",opcion,":",nombre_subopciones[opcion-1])
                                print(filtrado.sort_values(by=[opcion-1],ascending=[True]))
                            if opcion in [2,3,4]:
                                print("Se ordenara de acuerdo",opcion,":",nombre_subopciones[opcion-1])
                                print(filtrado.sort_values(by=[opcion],ascending=[True]))
                            else:
                                print("Ingresar una opcion valida del 1 al 4")

                            respuesta= input("Desea seguir ordenando datos? si/no: ")
                            if respuesta == "si":
                                continue
                            if respuesta == "no":
                                print("Fue un gusto servirle")
                                break

            ### estas son las lineas para ejecucion 
            mi_archivo= Archivo("MASCOTAS.csv")
            # mi_archivo.cargar_archivo()
            #mi_archivo.mostrar_datos("MASCOTAS.csv")
            mi_archivo.ordenar_datos("MASCOTAS.csv")
            

        else:
            print("Ejecutando Opcion 6")

        respuesta= input("Necesita realizar alguna otra operación? si/no: ")
        if respuesta == "si":
         continue
        if respuesta == "no":
            print("Estamos para servirle")
            break
