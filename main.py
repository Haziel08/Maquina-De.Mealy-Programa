from visual import interfaz
from logica import mealy_logica

def main():
    ejecutando = True
    
    while ejecutando:
        interfaz.mostrar_encabezado()
        opcion = interfaz.mostrar_menu_principal()
        
        if opcion == "1":
            mealy_logica.ejecucion_principal(interfaz)
        
        elif opcion == "2":
            print("\nSaliendo del programa...")
            print("¡Gracias por usar el programa!")
            ejecutando = False
        
        else:
            print("\nOpción no válida, intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()