# Lista para guardar las sesiones
sesiones = []

# Cantidad de sesiones a ingresar
cantidad = int(input("¿Cuántas sesiones desea registrar?: "))

# Ingreso de datos por el usuario
for i in range(cantidad):

    print(f"\n--- Sesión {i + 1} ---")

    id_cliente = input("Ingrese el ID del cliente: ")
    duracion = int(input("Ingrese la duración de la sesión en segundos: "))
    clics = int(input("Ingrese la cantidad de clics: "))

    # Guardar datos en la matriz
    sesiones.append([id_cliente, duracion, clics])


# clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Informe final
print("\n===== INFORME DE COMPROMISO =====")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print(f"Cliente: {id_cliente} -> Compromiso: {clasificacion}")