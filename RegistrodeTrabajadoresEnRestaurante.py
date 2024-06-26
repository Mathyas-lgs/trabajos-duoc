#Evaluación N°3: Registro de Trabajadores en Restaurante
# Mathyas Lagos

import csv

# Variables
nombre=""
apellido=""
cargo=""
sueldo_bruto=0
descuento_salud=0 
descuento_afp=0
sueldo_liquido=0
trabajador=[]
opcion=0
buscar=""
buscador=bool

def crear_csv():
    with open("trabajadores_restaurante.csv", "w", newline="") as archivo_csv:
        crear=csv.writer(archivo_csv)
        crear.writerow(["Nombre ", " Apellido ", " Cargo ", " Sueldo bruto", " Destinado a Salud", " Destinado a AFP", " Sueldo Liquido"])
crear_csv()
# Crea el csv para ir ingresando los datos

def mostrar_trabajadores():
    with open("trabajadores_restaurante.csv", "r", newline="") as archivo:
        leer=csv.reader(archivo)
        for datos in leer:
            print(datos)
# Nos permite ver los datos del csv


while True:
    print('''
    -----Registro de trabajadores-----------
    
    1) Registrar Trabajador
    2) Listar todos los Trabajadores
    3) Imprimir Planilla de Sueldos por Cargo
    4) Salir
    
    ----------------------------------------
        ''')
    
    opcion=input("Opcion: ")
    opcion.isnumeric()
    while opcion.isnumeric() == False :
        print("Opcion no valida")
        opcion=input("Opcion: ")
    opcion=int(opcion)  # Convierte opcion en un numero

    if opcion == 1 :
        nombre=input("Ingrese Nombre: ")
        apellido=input("Ingrese Apellido: ")

        print("Su Cargo tiene que ser: mesero, cocinero o cajero      # Escribalo como se muestra")
        cargo=input("Cual Es Su Cargo: ")
        cargo.lower()
        print(f"Esta encargado de ser: {cargo}")

        sueldo_bruto=input("Ingrese Sueldo Bruto: ")
        sueldo_bruto.isnumeric()
        while sueldo_bruto.isnumeric() == False :
            print("No ingreso un numero")
            sueldo_bruto=input("Ingrese Sueldo Bruto: ")
        sueldo_bruto=int(sueldo_bruto)

        descuento_salud=sueldo_bruto*0.07  # Calculamos cuanto de su sueldo se va a la salud
        descuento_afp= sueldo_bruto*0.10   # Calculamos cuanto de su sueldo se va a  AFK
        sueldo_liquido=sueldo_bruto - descuento_afp - descuento_salud  # Este sera el saldo que tendra

        trabajador.append(nombre)
        trabajador.append(apellido)
        trabajador.append(cargo)
        trabajador.append(sueldo_bruto)
        trabajador.append(descuento_salud)
        trabajador.append(descuento_afp)
        trabajador.append(sueldo_liquido)

        with open("trabajadores_restaurante.csv", "a", newline="") as archive:
            añadir_trabajador=csv.writer(archive)
            añadir_trabajador.writerow(trabajador)

        trabajador=[]

    elif opcion == 2 :
        mostrar_trabajadores()

    elif opcion == 3 :
        buscar=input(" ¿Que cargo busca?\n mesero, cocinero o cajero: \n")

        with open("trabajadores_restaurante.csv", "r", newline="") as buscar:
            buscador=csv.reader(buscar)

            if buscar == "mesero" :
                for filamesero in buscador:
                    print(filamesero[2])

            elif buscar == "cocinero" :
                for filacocinero in buscador:
                    print(filacocinero[2])
            
            elif buscar == "cajero" :
                for filacajero in buscador:
                    print(filacajero[2])

            else:
                print("No ingreso un cargo valido")

    elif opcion == 4 :
        print("Saliendo del Programa. Adios! ")
        break   