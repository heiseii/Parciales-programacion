#Programa de control de inventario - Ferreteria
herramientas = []
existencias = []

#Menu interactivo
while True:
    opcion = str(input("\nSeleccione una opción:\n1. Cargar herramientas\n2. Cargar stock\n3. Mostrar inventario\n4. Consulta de stock\n5. Reporte de agotados\n6. Alta de nuevo producto\n7. Actualizacion de stock (Venta/Ingreso)\n8. Salir\nOpción: "))
    
    #opcion 1 cargar herramientas
    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad de herramientas a cargar: "))
        i = 0
        while i < cantidad:
            herramienta = (input(f"Ingrese el nombre de la {i + 1}° herramienta: "))
            if herramienta == "":
                print("El nombre no puede estar vacío. Intente nuevamente.")
            elif herramienta in herramientas:
                print("La herramienta ya existe. Ingrese un nombre diferente: ")
            else:
                herramientas.append(herramienta)
                print("Herramienta cargada exitosamente.\n")
                existencias.append(0)
                print("Quiere cargar el stock ahora?\n1. Si\n2. No\n")
                cargar_stock = str(input("Opción: "))
                while not cargar_stock == "1" and not cargar_stock == "2":
                    cargar_stock = str(input("Opción no válida. Por favor, seleccione 1 para Si o 2 para No:\n "))
                if cargar_stock == "1":
                    existencias[-1] = int(input(f"Ingrese el stock para {herramienta}: "))
                    print("--Stock cargado exitosamente.--\n")
                i += 1
        

    #opcion 2 cargar stock
    elif opcion == "2":
        if len(herramientas) == 0:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero.")
        else:
            for i in range(len(herramientas)):
                print(f"Herramienta: {herramientas[i]}")
                cantidad = int(input(f"Ingrese la cantidad de stock a cargar para {herramientas[i]}: "))
                while cantidad < 0:
                    print("El valor debe ser un número entero positivo o cero.")
                    cantidad = int(input(f"Ingrese la cantidad de stock a cargar para {herramientas[i]}: "))
                existencias[i] += cantidad
                print(f"Herramienta actualizada: {herramientas[i]} | Stock: {existencias[i]}\n")

    #opcion 3 mostrar inventario
    elif opcion == "3":
        if len(herramientas) == 0:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero.\n")
        else:
            print("Inventario de herramientas:\n")
            for i in range(len(herramientas)):
                print(f"- {herramientas[i]}: {existencias[i]} unidades")


    #opcion 4 consulta de stock
    elif opcion == "4" and len(herramientas) == 0:
        print("No hay herramientas cargadas. Por favor, cargue herramientas primero.\n")
    elif opcion == "4":
            opciones_lista = '\n '.join(herramientas)
            consulta = str(input(f"Ingrese el nombre de la herramienta para consultar su stock:\nOpciones:\n {opciones_lista}\n"))
            if consulta in herramientas:
                index = herramientas.index(consulta)
                print(f"Stock de {consulta.capitalize()}/s: {existencias[index]} unidades\n")
            elif consulta.lower() in herramientas:
                index = herramientas.index(consulta.lower())
                print(f"Stock de {consulta.capitalize()}/s: {existencias[index]} unidades\n")
            elif consulta.upper() in herramientas:
                index = herramientas.index(consulta.upper())
                print(f"Stock de {consulta.capitalize()}/s: {existencias[index]} unidades\n")
            elif consulta.capitalize() in herramientas:
                index = herramientas.index(consulta.capitalize())
                print(f"Stock de {consulta.capitalize()}/s: {existencias[index]} unidades\n")
            else:
                print("Herramienta no encontrada en el inventario.\n")
    
    #opcion 5 reporte de agotados
    elif opcion == "5":
        hay_agotados = False
        for i in range(len(herramientas)):
            if existencias[i] == 0:
                if not hay_agotados:
                    print("Herramientas agotadas:\n")
                print(f"- {herramientas[i]}")
                hay_agotados = True
        if not hay_agotados:
            print("No hay herramientas agotadas en el inventario.\n")


    #opcion 6 alta de nuevo producto
    elif opcion == "6":
        nueva_herramienta = str(input("Ingrese el nombre de la nueva herramienta: "))
        if nueva_herramienta == "":
            print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")
        elif nueva_herramienta.isalpha() == False:
            print("El nombre de la herramienta no puede contener números o caracteres especiales. Por favor, ingrese un nombre válido.")
        elif nueva_herramienta in herramientas:
            print("La herramienta ya existe. Ingrese un nombre diferente: ")
        else:
            nuevo_stock = int(input(f"Ingrese el stock para {nueva_herramienta}: "))
            if nuevo_stock < 0:
                print("El stock no puede ser negativo. Por favor, ingrese un valor válido.")
            else:
                herramientas.append(nueva_herramienta)
                existencias.append(nuevo_stock)
                print("--Herramienta y stock cargados exitosamente.--\n")

    #opcion 7 actualizacion de stock (venta/ingreso)
    elif opcion == "7":
        venta = str(input("¿Desea registrar una venta o un ingreso de stock?\n1. Venta\n2. Ingreso de stock\n3. Salir\nOpción: "))
        while venta != "1" and venta != "2" and venta != "3":
            venta = str(input("Opción no válida. Por favor, seleccione 1 para Venta o 2 para Ingreso de stock:\n "))
        if venta == "1":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas. Por favor, cargue herramientas primero.\n")
            else:
                for i in range(len(herramientas)):
                    print(f"{i + 1}. {herramientas[i]}: {existencias[i]} unidades")
                seleccion = int(input("Seleccione el número de la herramienta para registrar la venta: "))
                while seleccion < 1 or seleccion > len(herramientas):
                    seleccion = int(input("Número no válido. Por favor, seleccione un número del listado: "))
                cantidad = int(input(f"Ingrese la cantidad vendida para {herramientas[seleccion - 1]}: "))
                if cantidad > existencias[seleccion - 1]:
                    print("No hay suficiente stock para registrar la venta. Por favor, ingrese una cantidad menor o igual al stock disponible.\n")
                else:
                    existencias[seleccion - 1] -= cantidad
                    print(f"Venta registrada: {herramientas[seleccion - 1]} | Stock restante: {existencias[seleccion - 1]}\n")
        elif venta == "2":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas. Por favor, cargue herramientas primero.\n")
            else:
                for i in range(len(herramientas)):
                    print(f"{i + 1}. {herramientas[i]}: {existencias[i]} unidades")
                seleccion = int(input("Seleccione el número de la herramienta para registrar el ingreso de stock: "))
                while seleccion < 1 or seleccion > len(herramientas):
                    seleccion = int(input("Número no válido. Por favor, seleccione un número del listado: "))
                cantidad = int(input(f"Ingrese la cantidad de stock a ingresar para {herramientas[seleccion - 1]}: "))
                existencias[seleccion - 1] += cantidad
                print(f"Stock actualizado: {herramientas[seleccion - 1]} | Stock actual: {existencias[seleccion - 1]}\n")
        elif venta == "3":
            print("Saliendo del menú de actualización de stock.\n")

    #opcion 8 salir
    elif opcion == "8":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 8.\n")