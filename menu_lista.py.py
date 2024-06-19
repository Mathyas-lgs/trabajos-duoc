opcion=0
vehiculos_lista=[]
datos_vehiculos=[]
tipo_vehiculo=""
patente=""
marca=""
precio=0
multas=0
fecha_vehiculo=""
nombre_dueño_vehiculo=""
buscador=bool

while True:
    print('''
---------- MENU AUTOMOTORA ----------
        1)Grabar
        2)Buscar
        3)Imprimir Certificados
        4)Modificar
        5)Eliminar
        6)Salir
-------------------------------------
        ''')
    opcion=input("Opcion: ")
    opcion.isnumeric()
    while opcion.isnumeric() == False:
        print("Opcion no valida.")
        opcion=input("Opcion: ")
    opcion=int(opcion)

    if opcion == 6 :
        print("ADIOS!!")

    elif opcion == 1 :
        tipo_vehiculo=input("Ingrese tipo de vehiculo: ")
        patente=input("Ingrese patente: ")
        marca=input("Ingrese la marca: ")

        precio=input("Ingrese el precio: ")
        precio.isnumeric()
        while precio.isnumeric() == False:
            print("No ingreso un numero.")
            precio=input("Ingrese el precio: ")
        precio=int(precio)
        while precio < 5000000 :
            print("El precio debe ser mayor que los $ 5.000.000")
            precio=int(input("Ingrese el precio: "))

        opcion=input("tiene multas?   (1-si / 2-no) ")
        if opcion == 1 :
            multas=input("Ingrese el monto de la multa: ")
        else:
            multas=0

        fecha_vehiculo=input("Ingrese la fecha del registro del vehiculo: ")
        nombre_dueño_vehiculo=input("Ingrese el nombre del dueño del vehiculo: ")

        datos_vehiculos.append(tipo_vehiculo)
        datos_vehiculos.append(patente)
        datos_vehiculos.append(marca)
        datos_vehiculos.append(precio)
        datos_vehiculos.append(multas)
        datos_vehiculos.append(fecha_vehiculo)
        datos_vehiculos.append(nombre_dueño_vehiculo)
        vehiculos_lista.append(datos_vehiculos) #Los guarda en esta lista
        datos_vehiculos=[]  #REINICIA LOS DATOS DE ESTA LISTA , PARA PODER INGRESAR OTRO VEHICULO
        print("Datos registrados!!!")
    elif opcion == 2 : 
        patente=input("Ingrese la patente para buscarla: ")
        buscador=False       #why buscador?¿?¿?
        for i  in vehiculos_lista :
            if i[1] == patente:
                print(f'''
            Tipo de vehiculo: {i[0]}
            Patente: {i[1]}
            Marca: {i[2]}
            Precio: {i[3]}
            Multas: {i[4]}
            Fecha de registro del vehículo: {i[5]}
            Nombre del dueño: {i[6]}
                ''')
                buscador=True
                break       
        if buscador == False:
                print("No esta en el registro")
    
    elif opcion == 4 :
        patente=input("Ingrese la patente para encontrar el vehiculo: ")
        buscador=False
        for i in vehiculos_lista:
            if i[1] == patente:
                print(f'''
            Tipo de vehiculo: {i[0]}
            Patente: {i[1]}
            Marca: {i[2]}
            Precio: {i[3]}
            Multas: {i[4]}
            Fecha de registro del vehículo: {i[5]}
            Nombre del dueño: {i[6]}
                ''')
                buscador = True
            if buscador == True:
                while True: 
                    print('''
            --------QUE DESEA MODIFICAR----
            1)Tipo de vehiculo: 
            2)Patente: 
            3)Marca: 
            4)Precio: 
            5)Multas: 
            6)Fecha de registro del vehículo: 
            7)Nombre del dueño: 
            8)Volver a menu principal
                    ''')
                    opcion=input("Opcion: ")
                    opcion.isnumeric()
                    while opcion.isnumeric() == False:
                        print("Opcion no valida.")
                        opcion=input("Opcion: ")
                    opcion=int(opcion)

                    if opcion == 1 :
                        print("hola")
    elif opcion == 5 :
        patente=input("Ingrese la patente para eliminarla: ")
        buscador=False
        for i in vehiculos_lista :
            if i[1] == patente:
                print(f'''
            Tipo de vehiculo: {i[0]}
            Patente: {i[1]}
            Marca: {i[2]}
            Precio: {i[3]}
            Multas: {i[4]}
            Fecha de registro del vehículo: {i[5]}
            Nombre del dueño: {i[6]}
                ''')
                buscador=True
        if buscador == True:
            opcion=input("¿Seguro que desea eliminarlo?  (1-si/2-no)  ")
            opcion.isnumeric()
            while opcion.isnumeric() == False:
                print("Opcion no valida.")
                opcion=input("¿Seguro que desea eliminarlo?  (1-si/2-no)  ")
            opcion=int(opcion)
            if opcion == 1 :
                vehiculos_lista.pop(i)
                print("Registro borrado")
            elif opcion == 2 :
                break
        elif buscador == False:
                print("No esta en el registro")