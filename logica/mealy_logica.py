import math
import itertools

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


def generar_filas_transicion(num_estados, lista_codigos, nombres_entradas, nombres_salidas):
    """
    Genera las filas prellenadas para la tabla de transición (R4).
    """
    # 1. Generamos todas las combinaciones de las entradas (0 y 1)
    num_bits_entrada = len(nombres_entradas)
    combinaciones_entrada = list(itertools.product([0, 1], repeat=num_bits_entrada))
    
    filas = []
    
    # 2. Por cada estado, recorremos cada combinación de entrada
    for i in range(num_estados):
        nombre_edo_act = f"S{i}"
        codigo_edo_act = lista_codigos[i]
        
        for comb in combinaciones_entrada:
            # Construimos la parte de 'Estado Actual' (Nombre + Bits)
            fila = [nombre_edo_act, codigo_edo_act]
            
            # Agregamos los bits de las entradas
            fila.extend(list(comb))
            
            # Agregamos espacios vacíos para 'Estado Siguiente' y 'Salidas'
            fila.append("-") # Nombre Edo. Sig
            fila.append("-") # Código Edo. Sig
            
            # Tantos guiones como salidas tenga el sistema
            for _ in nombres_salidas:
                fila.append("-")
            
            filas.append(fila)
            
    return filas

def generar_tablas_verdad_r5(num_ff, nombres_entradas, nombres_salidas, lista_codigos, num_estados):
    """
    Prepara la estructura de las tablas de verdad para cada bit de FF y cada salida.
    """
    import itertools
    
    # Combinaciones de entradas (0, 1)
    combinaciones_ent = list(itertools.product([0, 1], repeat=len(nombres_entradas)))
    
    # Cabeceras para los bits del estado actual: qn, qn-1... q0
    cabecera_bits_act = [f"q{i}" for i in range(num_ff-1, -1, -1)]
    cabecera_completa_izq = cabecera_bits_act + nombres_entradas
    
    # Diccionario para guardar cada tabla
    tablas_resultados = {}

    # 1. Crear estructura para cada Flip-Flop (D)
    for i in range(num_ff):
        nombre_ff = f"D{num_ff - 1 - i}"
        filas = []
        for edo_idx in range(num_estados):
            cod_act = list(lista_codigos[edo_idx])
            for comb_ent in combinaciones_ent:
                # Parte izquierda: Bits de estado actual + bits de entrada
                fila = cod_act + list(comb_ent) + ["-"] # El guion es el valor de D
                filas.append(fila)
        tablas_resultados[nombre_ff] = {"cabecera": cabecera_completa_izq + [nombre_ff], "filas": filas}

    # 2. Crear estructura para cada Salida
    for sal_nombre in nombres_salidas:
        filas = []
        for edo_idx in range(num_estados):
            cod_act = list(lista_codigos[edo_idx])
            for comb_ent in combinaciones_ent:
                fila = cod_act + list(comb_ent) + ["-"] # El guion es el valor de la salida
                filas.append(fila)
        tablas_resultados[sal_nombre] = {"cabecera": cabecera_completa_izq + [sal_nombre], "filas": filas}

    return tablas_resultados

def ejecucion_principal(interfaz):
    interfaz.mostrar_encabezado()
    
    # --- PASO 1: ENTRADAS ---
    print("\n--- CONFIGURACIÓN DE ENTRADAS ---")
    num_entradas = leer_entero("¿Cuántas entradas binarias tiene el sistema?: ")
    nombres_entradas = [input(f"  -> Nombre de entrada {i+1}: ") for i in range(num_entradas)]
    
    # --- PASO 2: SALIDAS ---
    print("\n--- CONFIGURACIÓN DE SALIDAS ---")
    num_salidas = leer_entero("¿Cuántas salidas binarias tiene el sistema?: ")
    nombres_salidas = [input(f"  -> Nombre de salida {i+1}: ") for i in range(num_salidas)]

    # --- PASO 3: ESTADOS ---
    print("\n--- CONFIGURACIÓN DE ESTADOS ---")
    num_estados = leer_entero("¿Cuántos estados tiene la máquina (N)?: ")

    # --- PASO 4: CODIFICACIÓN ---
    print("\n--- SELECCIÓN DE CODIFICACIÓN ---")
    print("1. Binario\n2. Gray\n3. One-Hot")
    while True:
        opcion_cod = leer_entero("Seleccione una opción: ")
        if 1 <= opcion_cod <= 3: break
        print("Opción no válida.")

    tipos = {1: "Binario", 2: "Gray", 3: "One-Hot"}
    codificacion_elegida = tipos[opcion_cod]
    
    # --- CÁLCULOS INTERNOS ---
    num_ff = calcular_cantidad_ff(num_estados, opcion_cod)
    lista_codigos = generar_codigos_estados(num_estados, opcion_cod, num_ff)
    
    # --- RESUMEN CONSOLIDADO ---
    interfaz.mostrar_encabezado() 
    print("\n" + "="*50)
    print("             RESUMEN DEL SISTEMA")
    print("="*50)
    print(f"Entradas:      {', '.join(nombres_entradas)}")
    print(f"Salidas:       {', '.join(nombres_salidas)}")
    print(f"Estados:       {num_estados}")
    print(f"Codificación:  {codificacion_elegida}")
    print(f"Flip-Flops:    {num_ff}")
    print("-"*50)
    
    # Diagrama de Bloques
    interfaz.dibujar_diagrama_bloques(nombres_entradas, nombres_salidas)
    
    # Tabla de Codificación (Asignación de estados)
    print("\nASIGNACIÓN DE ESTADOS (BIT POR ESTADO):")
    datos_tabla_cod = [[f"S{i}", lista_codigos[i]] for i in range(num_estados)]
    interfaz.imprimir_tabla(datos_tabla_cod, ["Estado", "Código"])
    
    input("\nPresione Enter para ver las Tablas de Transición y Verdad...")

    # --- TABLA DE TRANSICIÓN PRELLENADA ---
    interfaz.mostrar_encabezado()
    print("\n" + "="*60)
    print("         TABLA DE TRANSICIÓN (PRELLENADO)")
    print("="*60)
    
    cabecera_trans = ["Edo. Act.", "Bits (q)"] + nombres_entradas + ["Edo. Sig.", "Bits (D)"] + nombres_salidas
    filas_transicion = generar_filas_transicion(num_estados, lista_codigos, nombres_entradas, nombres_salidas)
    interfaz.imprimir_tabla(filas_transicion, cabecera_trans)
    
    # --- TABLAS DE VERDAD ---
    print("\n" + "="*60)
    print("         ESTRUCTURAS PARA TABLAS DE VERDAD")
    print("="*60)
    
    tablas_r5 = generar_tablas_verdad_r5(num_ff, nombres_entradas, nombres_salidas, lista_codigos, num_estados)

    print("\n[ ENTRADAS DE LOS FLIP-FLOPS ]")
    for nombre, contenido in tablas_r5.items():
        if nombre.startswith("D"):
            print(f"\nTabla para {nombre}:")
            interfaz.imprimir_tabla(contenido["filas"], contenido["cabecera"])

    print("\n[ SALIDAS DEL SISTEMA ]")
    for nombre, contenido in tablas_r5.items():
        if nombre in nombres_salidas:
            print(f"\nTabla para {nombre}:")
            interfaz.imprimir_tabla(contenido["filas"], contenido["cabecera"])

    print("\nLos espacios marcados con '-' deben completarse según el diseño de la máquina.")
    input("\nPresione Enter para regresar al menú principal...")