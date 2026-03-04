from tabulate import tabulate
import os

def mostrar_encabezado():
    # Limpiamos pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("       Ibares Sanchez Haziel - Primer Examen")
    print("       Generador de Máquinas de Mealy")
    print("="*50)

def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ingresar datos del problema")
    print("2. Salir")
    opcion = input("\nSeleccione una opción: ")
    return opcion

def dibujar_diagrama_bloques(entradas, salidas):
    """
    Dibuja un diagrama de bloques ASCII dinámico (R1).
    Muestra entradas a la izquierda y salidas a la derecha.
    """
    print("\n(R1) DIAGRAMA A BLOQUES:")
    
    # Determinamos cuántas líneas tendrá el diagrama según el mayor número de pines
    max_lineas = max(len(entradas), len(salidas))
    
    # Techo del bloque
    print(f"{' ':>12}  _______________________")
    
    for i in range(max_lineas):
        # Lógica para mostrar nombre de entrada o espacio vacío
        etiqueta_ent = entradas[i] if i < len(entradas) else ""
        flecha_ent = "--->" if i < len(entradas) else "    "
        
        # Lógica para mostrar nombre de salida o espacio vacío
        etiqueta_sal = salidas[i] if i < len(salidas) else ""
        flecha_sal = "--->" if i < len(salidas) else ""
        
        # Texto central del bloque (solo en la línea media o distribuido)
        contenido_bloque = "       MEALY       " if i == max_lineas // 2 else "                   "
        
        # Construcción de la línea
        # {etiqueta_ent:>8} alinea el nombre a la derecha en 8 espacios
        print(f"{etiqueta_ent:>10} {flecha_ent}|{contenido_bloque}|{flecha_sal} {etiqueta_sal}")

    # Piso del bloque
    print(f"{' ':>12} |_______________________|")

def imprimir_tabla(datos, encabezados):
    """
    Recibe una lista de listas y los nombres de las columnas,
    y los imprime en formato de tabla ASCII (R2/R4).
    """
    print(tabulate(datos, headers=encabezados, tablefmt="grid"))