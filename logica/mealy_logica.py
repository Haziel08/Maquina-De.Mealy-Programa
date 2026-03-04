def leer_entero(mensaje):
    """
    Pide un valor al usuario y verifica que sea un número entero.
    Si el usuario ingresa texto o símbolos, vuelve a preguntar.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero.")

def ejecucion_principal(interfaz):
    interfaz.mostrar_encabezado()
    
    # --- PASO 1: CONFIGURACIÓN DE ENTRADAS ---
    print("\n--- PASO 1: CONFIGURACIÓN DE ENTRADAS ---")
    # Usamos nuestro nuevo método para validar
    num_entradas = leer_entero("¿Cuántas entradas binarias tiene el sistema?: ")
    
    nombres_entradas = []
    for i in range(num_entradas):
        nombre = input(f"  -> Ingrese el nombre para la entrada {i+1}: ")
        nombres_entradas.append(nombre)
    
    # --- PASO 2: CONFIGURACIÓN DE SALIDAS ---
    print("\n--- PASO 2: CONFIGURACIÓN DE SALIDAS ---")
    # Volvemos a usar el método para validar
    num_salidas = leer_entero("¿Cuántas salidas binarias tiene el sistema?: ")
    
    nombres_salidas = []
    for i in range(num_salidas):
        nombre = input(f"  -> Ingrese el nombre para la salida {i+1}: ")
        nombres_salidas.append(nombre)
    
    # --- VERIFICACIÓN TOTAL ---
    print("\n" + "="*30)
    print("[ VERIFICACIÓN DE DATOS ]")
    print(f"Entradas ({num_entradas}): {nombres_entradas}")
    print(f"Salidas  ({num_salidas}): {nombres_salidas}")
    print("="*30)
    
    print("\nTodos los nombres han sido validados y capturados.")
    input("\nPresione Enter para volver al menú...")