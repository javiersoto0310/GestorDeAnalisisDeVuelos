from gestor import GestorDeVuelos
from utilidades import limpiar_pantalla, mostrar_menu
from funciones_para_crear_graficos import graficar_clases_vuelo, graficar_pasajeros
import _csv
import os

if __name__ == "__main__":
    gestor = GestorDeVuelos("data/2021-informe-ministerio.csv")

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            print("-" * 130)
            print("INFORMACIÓN GENERAL AÑO 2021")
            print("-" * 130)
            print("Total vuelos:", len(gestor.lista))
            print("Domésticos:", gestor.vuelos_por_tipo("Domestico"))
            print("Internacionales:", gestor.vuelos_por_tipo("Internacional"))
            print("Aterrizajes:", gestor.total_movimientos("Aterrizaje"))
            print("Despegues:", gestor.total_movimientos("Despegue"))
            print("Total pasajeros:", gestor.total_pasajeros())
            input("\nPresione ENTER para continuar...")

        elif opcion == "2":
            try:
                limpiar_pantalla()
                print("Ingrese las fechas en formato DD/MM/2021")
                f1 = input("Desde: ")
                f2 = input("Hasta: ")
                vuelos_fecha = gestor.vuelos_por_fecha(f1, f2)

                print("\nCIUDADES DISPONIBLES:")
                ciudades = gestor.aeropuertos.obtener_ciudades_disponibles()
                for i, ciudad in enumerate(ciudades, 1):
                    print(f"{i}. {ciudad.title()}")

                seleccion = input("\nSeleccione el número de la ciudad: ")
                if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(ciudades)):
                    print("\nSelección inválida. Intente nuevamente.")
                    input("\nPresione ENTER para continuar...")
                    continue

                ciudad_elegida = ciudades[int(seleccion) - 1]
                vuelos_ciudad = gestor.filtrar_por_aeropuerto(vuelos_fecha, ciudad_elegida)
                resultados = []

                if not vuelos_ciudad:
                    print("\nNo se encontraron vuelos para esa ciudad en ese rango de fechas.")
                else:
                    print(f"\nResultados para {ciudad_elegida.title()}:")
                    print("Cantidad de vuelos:", len(vuelos_ciudad))
                    print("Aterrizajes:", gestor.movimientos(vuelos_ciudad, "Aterrizaje"))
                    print("Despegues:", gestor.movimientos(vuelos_ciudad, "Despegue"))
                    print("\nClases de vuelos:")
                    for tipo, cantidad in gestor.clases_de_vuelo(vuelos_ciudad).items():
                        print(f"  {tipo}: {cantidad}")
                        resultados.append((tipo, cantidad))

                    graficar_clases_vuelo(resultados, ciudad_elegida)

                    guardar = input("\n¿Desea guardar los resultados en un archivo CSV? (s/n): ").lower()
                    if guardar == "s":
                        os.makedirs("consultas", exist_ok=True)
                        nombre_archivo = f"consultas/resultados_vuelos_{ciudad_elegida.lower().replace(' ', '_')}.csv"
                        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo_csv:
                            writer = _csv.writer(archivo_csv)
                            writer.writerow([f"Resultados para {ciudad_elegida.title()}"])
                            writer.writerow(["Tipo de vuelo", "Cantidad"])
                            writer.writerows(resultados)
                        print(f"\nArchivo guardado como '{nombre_archivo}'")

                input("\nPresione ENTER para continuar...")

            except ValueError:
                print("\nFormato de fecha incorrecto. Intente nuevamente.")
                input("\nPresione ENTER para continuar...")

        elif opcion == "3":
            try:
                limpiar_pantalla()
                print("Ingrese las fechas en formato DD/MM/2021")
                f1 = input("Desde: ")
                f2 = input("Hasta: ")
                vuelos_fecha = gestor.vuelos_por_fecha(f1, f2)

                print("\nCIUDADES DISPONIBLES:")
                ciudades = gestor.aeropuertos.obtener_ciudades_disponibles()
                for i, ciudad in enumerate(ciudades, 1):
                    print(f"{i}. {ciudad.title()}")

                seleccion = input("\nSeleccione el número de la ciudad: ")
                if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(ciudades)):
                    print("\nSelección inválida. Intente nuevamente.")
                    input("\nPresione ENTER para continuar...")
                    continue

                ciudad_elegida = ciudades[int(seleccion) - 1]
                vuelos_ciudad = gestor.filtrar_por_aeropuerto(vuelos_fecha, ciudad_elegida)

                if not vuelos_ciudad:
                    print("\nNo se encontraron vuelos para esa ciudad en ese rango de fechas.")
                else:
                    cantidad = gestor.pasajeros(vuelos_ciudad)
                    abordaron = gestor.pasajeros_abordaron(vuelos_ciudad)
                    descendieron = gestor.pasajeros_descendieron(vuelos_ciudad)

                    print(f"\nResultados para {ciudad_elegida.title()}:")
                    print("Total pasajeros:", cantidad)
                    print("Pasajeros que abordaron:", abordaron)
                    print("Pasajeros que descendieron:", descendieron)
                    print("Promedio por vuelo:", round(cantidad / len(vuelos_ciudad)))
                    print("\nAerolíneas utilizadas:")
                    aerolineas = gestor.aerolineas_usadas(vuelos_ciudad)
                    for aer in aerolineas:
                        print("-", aer)

                    graficar_pasajeros(abordaron, descendieron, ciudad_elegida)

                    guardar = input("\n¿Desea guardar los resultados en un archivo CSV? (s/n): ").lower()
                    if guardar == "s":
                        os.makedirs("consultas", exist_ok=True)
                        nombre_archivo = f"consultas/resultados_pasajeros_{ciudad_elegida.lower().replace(' ', '_')}.csv"
                        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo_csv:
                            writer = _csv.writer(archivo_csv)
                            writer.writerow([f"Resultados para {ciudad_elegida.title()}"])
                            writer.writerow(["Total pasajeros", cantidad])
                            writer.writerow(["Pasajeros que abordaron", abordaron])
                            writer.writerow(["Pasajeros que descendieron", descendieron])
                            writer.writerow(["Promedio de pasajeros por vuelo", round(cantidad / len(vuelos_ciudad))])
                            writer.writerow([])
                            writer.writerow(["Aerolíneas utilizadas"])
                            for aer in aerolineas:
                                writer.writerow([aer])
                        print(f"\nArchivo guardado como '{nombre_archivo}'")
                input("\nPresione ENTER para continuar...")
            except ValueError:
                print("\nFormato de fecha incorrecto. Intente nuevamente.")
                input("\nPresione ENTER para continuar...")

        elif opcion == "4":
            limpiar_pantalla()
            print("TOP 10 AEROLÍNEAS MÁS USADAS")
            for nombre, cant in gestor.ranking_aerolineas():
                print(f"{nombre}: {cant} vuelos")
            input("\nPresione ENTER para continuar...")

        elif opcion == "5":
            limpiar_pantalla()
            print("\nCIUDADES DISPONIBLES:")
            ciudades = gestor.aeropuertos.obtener_ciudades_disponibles()
            for i, ciudad in enumerate(ciudades, 1):
                print(f"{i}. {ciudad.title()}")

            seleccion = input("\nIngrese el número de ciudad del aeropuerto: ")
            if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(ciudades)):
                print("\nSelección inválida. Intente nuevamente.")
                input("\nPresione ENTER para continuar...")
                continue
            ciudad_elegida = ciudades[int(seleccion) - 1]
            top_destinos = gestor.destinos_mas_frecuentes(ciudad_elegida)
            if not top_destinos:
                print(f"\nNo se encontraron destinos frecuentes para {ciudad_elegida.title()}.")
            else:
                print(f"\nTOP DESTINOS MÁS FRECUENTES DESDE {ciudad_elegida.title()}:")
                for destino, cant in top_destinos:
                    print(f"{destino}: {cant} vuelos")

            input("\nPresione ENTER para continuar...")

        elif opcion == "6":
            limpiar_pantalla()
            print("ESTADÍSTICAS POR MATRÍCULA (AVIÓN)")
            estadisticas = gestor.estadisticas_por_matricula()
            if not estadisticas:
                print("\nNo se encontraron registros de matrículas.")
            else:
                print("\nTOP MATRÍCULAS CON MÁS VUELOS:")
                for matricula, cant in estadisticas:
                    print(f"{matricula}: {cant} vuelos")
            input("\nPresione ENTER para continuar...")


        elif opcion == "7":
            limpiar_pantalla()
            print("VUELOS POR MES")
            vuelos_mes = gestor.vuelos_por_mes()
            for mes_anio, cant in vuelos_mes.items():
                print(f"{mes_anio}: {cant} vuelos")
            input("\nPresione ENTER para continuar...")

        elif opcion == "8":
            limpiar_pantalla()
            dia, cant = gestor.dia_mayor_actividad()
            print(f"DÍA CON MÁS VUELOS: {dia} ({cant} vuelos)")
            input("\nPresione ENTER para continuar...")

        elif opcion == "9":
            print("\nGracias por utilizar el sistema. Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            input("\nPresione ENTER para continuar...")
