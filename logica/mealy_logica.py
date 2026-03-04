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
    num_entradas = leer_entero("¿Cuántas entradas binarias tiene el sistema?: ")
    
    nombres_entradas = []
    for i in range(num_entradas):
        nombre = input(f"  -> Ingrese el nombre para la entrada {i+1}: ")
        nombres_entradas.append(nombre)
    
    # --- PASO 2: CONFIGURACIÓN DE SALIDAS ---
    print("\n--- PASO 2: CONFIGURACIÓN DE SALIDAS ---")
    num_salidas = leer_entero("¿Cuántas salidas binarias tiene el sistema?: ")
    
    nombres_salidas = []
    for i in range(num_salidas):
        nombre = input(f"  -> Ingrese el nombre para la salida {i+1}: ")
        nombres_salidas.append(nombre)

    # --- PASO 3: NÚMERO DE ESTADOS ---
    print("\n--- PASO 3: CONFIGURACIÓN DE ESTADOS ---")
    num_estados = leer_entero("¿Cuántos estados tiene la máquina (N)?: ")

    # --- PASO 4: MENÚ DE CODIFICACIÓN ---
    print("\n--- PASO 4: SELECCIÓN DE CODIFICACIÓN ---")
    print("1. Binario")
    print("2. Gray")
    print("3. One-Hot")
    
    # Validamos que la opción esté entre 1 y 3
    while True:
        opcion_cod = leer_entero("Seleccione el tipo de codificación: ")
        if 1 <= opcion_cod <= 3:
            break
        print("Error: Opción no válida. Elija 1, 2 o 3.")

    # Guardamos el nombre de la codificación
    tipos = {1: "Binario", 2: "Gray", 3: "One-Hot"}
    codificacion_elegida = tipos[opcion_cod]
    
    # --- VERIFICACIÓN FINAL ---
    interfaz.mostrar_encabezado() 
    print("\n" + "="*40)
    print("[ RESUMEN DE CONFIGURACIÓN ]")
    print(f"Entradas: {nombres_entradas}")
    print(f"Salidas:  {nombres_salidas}")
    print(f"Estados:  {num_estados}")
    print(f"Codificación elegida: {codificacion_elegida}")
    print("="*40)
    
    interfaz.dibujar_diagrama_bloques(nombres_entradas, nombres_salidas)
    
    print("\nDiagrama generado según los nombres proporcionados.")
    input("\nPresione Enter para volver al menú...")