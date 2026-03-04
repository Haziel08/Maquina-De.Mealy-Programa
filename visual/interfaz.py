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

def dibujar_bloques(entradas, salidas):
    print("\n(R1) DIAGRAMA A BLOQUES")
    print("      " + "_"*25)
    max_len = max(len(entradas), len(salidas))
    for i in range(max_len):
        ent = entradas[i].strip() if i < len(entradas) else ""
        sal = salidas[i].strip() if i < len(salidas) else ""
        flecha_ent = "--->" if ent else "    "
        flecha_sal = "--->" if sal else ""
        print(f"{ent:>10} {flecha_ent}|   MÁQUINA MEALY   |{flecha_sal} {sal}")
    print("      " + "‾"*25)

def imprimir_tabla(filas, encabezados):
    print(tabulate(filas, headers=encabezados, tablefmt="grid"))