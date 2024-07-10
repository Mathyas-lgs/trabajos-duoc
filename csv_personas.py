
# Este es un csv que guarda a las personas, sus apellido y su edad
# By: Mathyas Lagos

import csv

nombre= ""    # Nombre de la persona
apellido= ""  # Apellido de la persona
edad= 0       # Edad de la persona
rut=""
persona= []   # Donde se guardan los datos de la persona

opcion= 0

# Funcion que Creara el Archivo csv para registrar los datos
def crear_csv():
    try:
        with open("csv_de_personas.csv", "r", newline="") as archivo_csv:
            crear=csv.reader(archivo_csv)
            for line in crear:
                persona.append(line)
    except FileNotFoundError :
        with open("csv_de_personas.csv", "w", newline="") as archivo:
            crear=csv.writer(archivo) 
            crear.writerow(["Nombre", "Apellido", "Edad", "Rut"])
crear_csv()


# Funcion para verificar que el rut no sea igual a otro
def verificar_rut(rut):
    try:
        with open("csv_de_personas.csv", "r", newline="") as archivo :
            leer= csv.reader(archivo)
            next(leer)  # Omite la primera linea
            for linea in leer:
                if linea[3] == rut :
                    return True
    except FileNotFoundError:
        pass #  No hay otro rut igual
    return False

while True :
    print('''   
                    MENU
    -----------------------------------------
        1. Registrar Persona
        2. Ver CSV De Personas
        3. Editar Persona 
        4. Cerrar Programa
    -----------------------------------------

''')
    
    opcion=input("Opcion: ")
    while opcion.isnumeric() == False:
        print("Opcion no Valida.")
        opcion=input("Opcion: ")
    opcion=int(opcion) 

    if opcion == 1 :
        nombre=input("Nombre: ")
        apellido=input("Apellido : ")
        edad=input("Edad: ")
        while edad.isnumeric() == False:
            print("Ingrese un numero valido")
            edad=input("Edad: ")
        edad=int(edad)
        rut=input("Rut: ")
        if verificar_rut(rut):
            print("Ese rut ya esta en el csv")
        else:
            # Guardamos los datos obtenidos en una lista
            persona_datos = [nombre, apellido, edad, rut]
            persona.append(persona_datos)
        print("Datos de la persona registrados.")

        with open("csv_de_personas.csv", "a", newline="") as archive:
            añadir_persona=csv.writer(archive)
            añadir_persona.writerow(persona_datos)

    elif opcion == 2 :
        with open("csv_de_personas.csv", "r", newline="") as archivoo:
            leer_csv=csv.reader(archivoo)

            for line in leer_csv:
                print(line)

    elif opcion == 3 :
        edit_persona=input("Ingrese el rut para encontrar a la persona: ")
        editar = False

        with open("csv_de_personas.csv", "r", newline="") as archivo_leer :
            leer_csv=list(csv.reader(archivo_leer))
        with open("csv_de_personas.csv", "w", newline="") as archivo_escribir:
            escribir_csv=csv.writer(archivo_escribir)
            escribir_csv.writerow(["Nombre", "Apellido", "Edad", "Rut"])

            for linea in leer_csv:
                if linea and linea[3] == edit_persona:
                    nombre=input("Nombre: ")
                    apellido=input("Apellido: ")
                    edad=input("Edad: ")
                    while not edad.isnumeric():
                        print("Esa no es una edad.")
                        edad=input("Edad: ")
                    edad=int(edad)
                    rut=edit_persona
                    persona_datos=[nombre, apellido, edad, rut]
                    escribir_csv.writerow(persona_datos)
                    editar = True
                    print(f"Se edito {nombre} {apellido}")
                else:
                    escribir_csv.writerow(linea)
        if not editar :
            print("No hay una persona con ese rut.")
    
        #### AAAAAAAAAAAAAAAH SE CLONAAAA
    elif opcion == 4:
        print("ADIOS :D ")

    else:
        print("Opcion no valida.")