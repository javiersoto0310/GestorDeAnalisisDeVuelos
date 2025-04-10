import os

def mostrar_menu():
    print("-" * 130)
    print(" " * 50, "VUELOS REGISTRADOS 2021")
    print("-" * 130)
    print("1. Información general del año 2021")
    print("2. Consultar movimientos y tipos de vuelos por ciudad y rango de fechas")
    print("3. Consultar cantidad de pasajeros y aerolíneas por ciudad y rango de fechas")
    print("4. Ranking de aerolíneas más usadas")
    print("5. Destinos más frecuentes desde un aeropuerto")
    print("6. Estadísticas por avión (matrícula)")
    print("7. Vuelos por mes")
    print("8. Día de mayor actividad aérea")
    print("9. Salir")
    print("-" * 130)

def limpiar_pantalla():
    try:
        if os.name == "nt":
            os.system("cls")
        elif "TERM" in os.environ:
            os.system("clear")
    except ValueError:
        pass
