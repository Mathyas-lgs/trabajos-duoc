import csv
import math
import random

# Lista De Trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

empleados=[]

# Funcion Para Asignar Precio a Los Trabajadores
def generar_sueldo_trabajadores():
    for nombres in trabajadores:
        sueldo = random.randint(300000, 2500000)
        empleados.append({"trabajador":nombres,
                          "sueldo":sueldo})
        
# Funcion Para Clasificar Los Sueldos Segun Su Monto
def clasificar_sueldos():
    if not empleados:
        print("No hay Empleados Registrados.")
        return
    
    sueldo_menor = []    # En esta lista se almacenara los sueldos menores a $800.000
    sueldo_medio = []    # En esta lista se almacenaran los sueldos entre $800.000 y $2.000.000
    sueldo_mayor = []    # En esta lista se almacenaran los sueldos superiores a $2.000.000

    for dinero in empleados:
        sueldo = dinero["sueldo"]
        if sueldo < 800000 :
            sueldo_menor.append(dinero["trabajador"])
            sueldo_menor.append(dinero["sueldo"])
        elif  800000 <= sueldo <= 2000000:
            sueldo_medio.append(dinero["trabajador"])
            sueldo_medio.append(dinero["sueldo"])
        else:
            sueldo_mayor.append(dinero["trabajador"])
            sueldo_mayor.append(dinero["sueldo"])

    print(f'''
        Sueldos Menores a $800.000:  
        {sueldo_menor}  

        -Sueldo Entre $800.000 y $2.000.000:
        {sueldo_medio}

        -Sueldo Superior a $2.000.000:
        {sueldo_mayor}
      ''')

# Funcion Para Ver Estadisticas De Los trabajadores
def ver_estadisticas():
    if not empleados:
        print("No hay Empleados Registrados.")
        return
    
##    sueldo_bajo = empleados[0]
##    sueldo_alto = empleados[0]
##    for iterar_sueldos in empleados:
##        sueldo = iterar_sueldos["sueldo"]
##        if sueldo["sueldo"] < sueldo_bajo["sueldo"] :
##            sueldo_bajo = sueldo
##        if sueldo["sueldo"] > sueldo_alto["sueldo"]:
##            sueldo_alto = sueldo
#    print(f"El sueldo mas bajo es: {sueldo_bajo}")
#    print(f"El sueldo mas alto es: {sueldo_alto}")
#    # nopude:(


    #La Media Geometrica de los Sueldos
    media_geometrica = 1
    for cantidad in empleados:
        media_geometrica *= cantidad["sueldo"]

    saldos_totales = len(empleados)
    media_geometrica = math.pow(media_geometrica, 1/saldos_totales)

    print(f"La media geometrica es: {media_geometrica}")

# Funcion Para Generar CSV
def reporte_de_sueldo():
    if not empleados:
        print("No hay empleados")
        return
    with open("Sueldos.csv", "w", newline="") as archivo:
        escribir_csv=csv.writer(archivo)
        escribir_csv.writerow(["Nombre empleado", "sueldo base", "descuento salud", "descuento afp", "sueldo liquido"])

    with open("sueldos.csv", "a", newline="") as archv:
        añardir_csv=csv.writer(archv)
        añardir_csv.writerow(empleados)

# Funcion del Menu
def menu():
    while True:
        print('''
    ------------ MENU ----------------          
        1. Asignar Sueldos Aleatorios
        2. Clasificar Sueldos
        3. Ver Estadisticas
        4. Reporte de Sueldos
        5. Salir del Programa
    ----------------------------------
              ''')        

        opcion=input("Opcion: ")
        if opcion.isnumeric():
            opcion=int(opcion)
            if opcion == 1 :
                generar_sueldo_trabajadores()
                print("Se Generaron Los Sueldos.")
            elif opcion == 2 :
                clasificar_sueldos()
            elif opcion == 3 :
                ver_estadisticas()
            elif opcion == 4 :
                reporte_de_sueldo()
            elif opcion == 5 :
                print("Finalizando programa...")
                print("Desarrollado por Mathyas Lagos")
                print("Rut 21.041.117-8")
                break
            else :
                print("Selecione una opcion valida porfavor.")
        else:
            print("Selecione una opcion valida porfavor.")

menu()  # Iniciamos el Menu
