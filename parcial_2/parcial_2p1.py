#|| Programa de gestion de inventario ||

#Sistema de menu
def menu():
    
    inventario = []
    while True:
        print("""-- Bienvenido al sistema de gestion de inventario para Ferreteria. --
    1. Cargar herramientas
    2. Mostrar inventario
    3. Consultar stock
    4. Reporte de agotados
    5. Agregar herramienta (Alta de productos)
    6. Actualizar stock (Venta / Ingreso)
    7. Salir""")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            cargar_herramientas(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            consultar_stock(inventario)
        elif opcion == "4": 
            reporte_agotados(inventario)
        elif opcion == "5":
            alta_producto(inventario)
        elif opcion == "6":
            actualizar_stock(inventario)
        elif opcion == "7":
            salir()
        else:
            print("Opcion no valida. Intente de nuevo.")
    

#Opcion 1: Cargar herramientas
def cargar_herramientas(inventario):
    # Si ya hay herramientas, redirigir a opción 5
    if len(inventario) > 0:
        print("El inventario ya tiene herramientas cargadas. Use la opcion 5 para agregar nuevas.")
        return

    # Pedir cantidad válida
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de herramientas a cargar: "))
            if cantidad <= 0:
                print("La cantidad debe ser un numero entero mayor a cero.")
                continue
            break
        except ValueError:
            print("Entrada no valida. Ingrese un numero entero.")

    # Cargar cada herramienta
    i = 0
    while i < cantidad:
        # Pedir y validar nombre
        try:
            nombre = input(f"Ingrese el nombre de la herramienta #{i+1}: ").strip()
            if nombre == "":
                raise ValueError("El nombre no puede estar vacio.")
            for item in inventario:
                if item['herramienta'].strip().lower() == nombre.lower():
                    raise ValueError(f"Ya existe una herramienta llamada '{nombre}'.")
        except ValueError as e:
            print(f"Error: {e}")
            continue  # vuelve a pedir el mismo i

        # Pedir y validar stock
        try:
            cantidad_stock = int(input(f"Ingrese el stock inicial de '{nombre}': "))
            if cantidad_stock < 0:
                raise ValueError("El stock no puede ser negativo.")
        except ValueError as e:
            print(f"Error: {e}")
            continue  # vuelve a pedir el mismo i

        inventario.append({'herramienta': nombre, 'cantidad': cantidad_stock})
        i += 1  # solo avanza si todo salió bien

    print("Herramientas cargadas exitosamente.")

# Opcion 2: Mostrar inventario                        
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        print("Inventario de herramientas:")
        for item in inventario:
            print(f"- {item['herramienta']}: {item['cantidad']} unidades")

# Opcion 3: Consultar stock
def consultar_stock(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return

    nombre = input("Ingrese el nombre de la herramienta a consultar: ").strip()
    for item in inventario:
        if item['herramienta'].strip().lower() == nombre.lower():
            print(f"Stock de '{item['herramienta']}': {item['cantidad']} unidades")
            return
    print(f"No se encontro la herramienta '{nombre}' en el inventario.")

# Opcion 4: Reporte de agotados
def reporte_agotados(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return

    agotados = [item for item in inventario if item['cantidad'] == 0]
    if len(agotados) == 0:
        print("No hay herramientas agotadas.")
    else:
        print("Herramientas agotadas:")
        for item in agotados:
            print(f"- {item['herramienta']}")

# Opcion 5: Agregar herramienta (Alta de productos)
def alta_producto(inventario):
    # Pedir y validar nombre
    try:
        nombre = input("Ingrese el nombre de la nueva herramienta: ").strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacio.")
        for item in inventario:
            if item['herramienta'].strip().lower() == nombre.lower():
                raise ValueError(f"Ya existe una herramienta llamada '{nombre}'.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Pedir y validar stock
    try:
        cantidad_stock = int(input(f"Ingrese el stock inicial de '{nombre}': "))
        if cantidad_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    inventario.append({'herramienta': nombre, 'cantidad': cantidad_stock})
    print(f"Herramienta '{nombre}' agregada exitosamente con {cantidad_stock} unidades.")

# Opcion 6: Actualizar stock (Compra / Venta)
def actualizar_stock(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return

    nombre = input("Ingrese el nombre de la herramienta a actualizar: ").strip()
    for item in inventario:
        if item['herramienta'].strip().lower() == nombre.lower():
            while True:
                eleccion = input("""
                Seleccione una opcion:
                1. Venta (disminuir stock)
                2. Ingreso (aumentar stock)
                3. Cancelar
                Opcion: """)
                if eleccion == "1":
                    try:
                        cantidad = int(input("Ingrese la cantidad a vender: "))
                        if cantidad <= 0:
                            raise ValueError("La cantidad debe ser un numero entero mayor a cero.")
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                    if cantidad > item['cantidad']:
                        print(f"No hay suficiente stock para vender {cantidad} unidades. Stock actual: {item['cantidad']}.")
                        continue
                    item['cantidad'] -= cantidad
                    print(f"Venta realizada. Nuevo stock de '{item['herramienta']}': {item['cantidad']} unidades.")
                    break
                elif eleccion == "2":
                    try:
                        cantidad = int(input("Ingrese la cantidad a ingresar: "))
                        if cantidad <= 0:
                            raise ValueError("La cantidad debe ser un numero entero mayor a cero.")
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                    item['cantidad'] += cantidad
                    print(f"Ingreso realizado. Nuevo stock de '{item['herramienta']}': {item['cantidad']} unidades.")
                    break
                elif eleccion == "3":
                    print("Actualizacion cancelada.")
                    break
                else:
                    print("Opcion no valida. Intente de nuevo.")
            return
        
# Opcion 7: Salir
def salir():
    print("Saliendo del programa...")
    exit()

menu()

