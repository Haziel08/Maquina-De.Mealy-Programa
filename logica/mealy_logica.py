import math

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


def calcular_cantidad_ff(num_estados, opcion_cod):
    if opcion_cod == 1 or opcion_cod == 2:
        # Usamos math.log2 y math.ceil para redondear hacia arriba
        return math.ceil(math.log2(num_estados))
    elif opcion_cod == 3:
        # En One-Hot, el número de FF es igual al número de estados
        return num_estados
    return 0

def generar_codigos_estados(num_estados, opcion_cod, n_ff):
    codigos = []
    
    for i in range(num_estados):
        if opcion_cod == 1:  # BINARIO
            # Convertimos a binario, quitamos '0b' y rellenamos con ceros
            codigo = bin(i)[2:].zfill(n_ff)
            
        elif opcion_cod == 2:  # GRAY
            # Fórmula de Gray: i XOR (i desplazado a la derecha)
            gray_val = i ^ (i >> 1)
            codigo = bin(gray_val)[2:].zfill(n_ff)
            
        elif opcion_cod == 3:  # ONE-HOT
            # Un '1' en la posición correspondiente y '0' en las demás
            # Usualmente el bit más significativo es el estado más alto
            lista_bits = ["0"] * num_estados
            lista_bits[num_estados - 1 - i] = "1"
            codigo = "".join(lista_bits)
            
        codigos.append(codigo)
    
    return codigos



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
    
    # --- PASO 5: CÁLCULO DE FLIP-FLOPS (R2) ---
    num_ff = calcular_cantidad_ff(num_estados, opcion_cod)
    
    # 2. Generamos los códigos de cada estado
    lista_codigos = generar_codigos_estados(num_estados, opcion_cod, num_ff)
    
    # 3. Preparar los datos para la tabla de la interfaz
    # Creamos una lista de listas: [['S0', '00'], ['S1', '01'], ...]
    datos_tabla_cod = []
    for i in range(num_estados):
        datos_tabla_cod.append([f"S{i}", lista_codigos[i]])

    # 4. Mostrar resultados
    interfaz.mostrar_encabezado()
    interfaz.dibujar_diagrama_bloques(nombres_entradas, nombres_salidas)
    
    print("\n" + "="*45)
    print(f"(R2) ANÁLISIS DE MEMORIA Y CODIFICACIÓN")
    print(f"Tipo: {codificacion_elegida} | FF necesarios: {num_ff}")
    print("="*45)
    
    # Usamos tabulate para que se vea como una tabla de examen
    print("\nTABLA DE ASIGNACIÓN DE ESTADOS:")
    interfaz.imprimir_tabla(datos_tabla_cod, ["Estado", "Código (Bits)"])
    
    input("\nPresione Enter para volver al menú...")