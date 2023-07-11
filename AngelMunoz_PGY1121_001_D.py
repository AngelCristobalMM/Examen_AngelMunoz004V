# Variables
pisos = 10
departamentos_por_piso = 4
precios = {"A": 3800, "B": 3000, "C": 2800, "D": 3500}
departamentos_disponibles = [[True] * departamentos_por_piso for _ in range(pisos)]
compradores = []

# Funciones
def mostrar_menu():
    print("------ Menu ------")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    print("-------------------")

def comprar_departamento():
    piso = int(input("Ingrese el número de piso (1-10): "))
    tipo = input("Ingrese el tipo de departamento (A, B, C o D): ").upper()

    departamento_fila = ord(tipo) - ord("A")
    departamento_columna = piso - 1

    if departamento_fila < 0 or departamento_fila >= departamentos_por_piso:
        print("Tipo de departamento invalido.")
        return

    if departamento_columna < 0 or departamento_columna >= pisos:
        print("Numero de piso invalido.")
        return

    if not departamentos_disponibles[departamento_columna][departamento_fila]:
        print("El departamento no está disponible.")
        return

    run = input("Ingrese el RUN del comprador (sin guion ni puntos): ")
    compradores.append({"RUN": run, "Tipo": tipo, "Piso": piso})
    departamentos_disponibles[departamento_columna][departamento_fila] = False
    print("Operación realizada correctamente.")

def mostrar_departamentos_disponibles():
    print("Departamentos disponibles:")
    for i in range(pisos):
        for j in range(departamentos_por_piso):
            estado = "X" if not departamentos_disponibles[i][j] else " "
            tipo = chr(ord("A") + j)
            piso = i + 1
            print(f"Tipo {tipo}{piso}: {estado}")

def mostrar_listado_compradores():
    compradores_ordenados = sorted(compradores, key=lambda x: x["RUN"])
    print("Listado de compradores:")
    for comprador in compradores_ordenados:
        print(f"RUN: {comprador['RUN']}, Tipo: {comprador['Tipo']}, Piso: {comprador['Piso']}")

def mostrar_ganancias_totales():
    ganancias_totales = 0
    ventas_por_tipo = {}

    for comprador in compradores:
        tipo = comprador["Tipo"]
        precio = precios[tipo]
        ganancias_totales += precio
        if tipo in ventas_por_tipo:
            ventas_por_tipo[tipo] += precio
        else:
            ventas_por_tipo[tipo] = precio

    print("Ventas totales por tipo de departamento:")
    for tipo, venta in ventas_por_tipo.items():
        print(f"Tipo {tipo}: {venta} UF")

    print(f"Total: {ganancias_totales} UF")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        comprar_departamento()
    elif opcion == "2":
        mostrar_departamentos_disponibles()
    elif opcion == "3":
        mostrar_listado_compradores()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        salir()