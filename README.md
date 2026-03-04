# Generador de Máquinas de Mealy

Este programa es una herramienta diseñada para automatizar los pasos del diseño de sistemas con Mealy. Permite generar diagramas a bloques, tablas de asignación de estados y las estructuras para las tablas de transición y de verdad en la terminal.

---

## Instalación y Requisitos

Para ejecutar este programa es necesario tener instalado Python 3.12 o una versión superior. Además, se requiere la librería tabulate para que las tablas se visualicen correctamente.

1. Descarga los archivos del proyecto.
2. Instalar la dependencia necesaria ejecutando:
   ```bash
   pip install tabulate

Para iniciar la aplicación, sitúate en la carpeta del proyecto y ejecuta el siguiente comando:

python main.py

Guía de Uso

Configuración de Pines: Ingresa los nombres de las entradas y salidas (ejemplo: C3, C2, C1, C0 para entradas y A, E para salidas).

Definición de Estados: Ingresa el número de estados totales de la máquina.

Selección de Codificación: Selecciona entre el método Binario, Gray u One-Hot.

Visualización: El sistema genera automáticamente el diagrama a bloques y las tablas. Los espacios marcados con un guion (-) corresponden a los valores que deben ser llenados según el diseño del diagrama de estados específico.