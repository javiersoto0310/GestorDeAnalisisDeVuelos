from datetime import datetime
from collections import Counter, defaultdict
import _csv
from aeropuerto import Aeropuerto

class GestorDeVuelos:
    def __init__(self, path_csv):
        self.lista = self._cargar_csv(path_csv)
        self.aeropuertos = Aeropuerto(self.lista)

    def _cargar_csv(self, path):
        with open(path, "r", encoding="UTF-8") as datos:
            entrada = _csv.reader(datos, delimiter=";")
            return list(entrada)[1:]

    def vuelos_por_tipo(self, tipo_vuelo):
        return sum(1 for v in self.lista if v[3] == tipo_vuelo)

    def total_movimientos(self, tipo_mov):
        return sum(1 for v in self.lista if v[4] == tipo_mov)

    def total_pasajeros(self):
        return sum(int(v[9]) for v in self.lista if v[9].isdigit())

    def vuelos_por_fecha(self, fecha1, fecha2):
        fecha_desde = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_hasta = datetime.strptime(fecha2, "%d/%m/%Y")
        return [v for v in self.lista if fecha_desde <= datetime.strptime(v[0], "%d/%m/%Y") <= fecha_hasta]

    def filtrar_por_aeropuerto(self, vuelos, nombre_ciudad):
        codigo_iata = self.aeropuertos.obtener_codigo_iata(nombre_ciudad)
        if not codigo_iata:
            return []
        return [v for v in vuelos if v[5].strip().upper() == codigo_iata]

    def movimientos(self, vuelos, tipo_vuelo):
        return sum(1 for v in vuelos if v[4] == tipo_vuelo)

    def pasajeros(self, vuelos):
        return sum(int(v[9]) for v in vuelos if v[9].isdigit())

    def pasajeros_abordaron(self, vuelos):
        return self.pasajeros([v for v in vuelos if v[4] == "Despegue"])

    def pasajeros_descendieron(self, vuelos):
        return self.pasajeros([v for v in vuelos if v[4] == "Aterrizaje"])

    def clases_de_vuelo(self, vuelos):
        conteo = {}
        for vuelo in vuelos:
            tipo_vuelo = vuelo[2].strip()
            conteo[tipo_vuelo] = conteo.get(tipo_vuelo, 0) + 1
        return conteo

    def aerolineas_usadas(self, vuelos):
        return sorted(set(v[7] for v in vuelos if v[7]))

    def ranking_aerolineas(self, top=10):
        conteo = Counter(v[7] for v in self.lista if v[7])
        return conteo.most_common(top)

    def destinos_mas_frecuentes(self, nombre_ciudad, top=10):
        codigo_iata = self.aeropuertos.obtener_codigo_iata(nombre_ciudad)
        if not codigo_iata:
            return []
        destinos = [v[6] for v in self.lista if v[5].strip().upper() == codigo_iata and v[4] == "Despegue" and v[6]]
        conteo = Counter(destinos)
        return conteo.most_common(top)

    def estadisticas_por_matricula(self, top=10):
        conteo = Counter(v[8] for v in self.lista if v[8])
        return conteo.most_common(top)

    def vuelos_por_mes(self):
        conteo = defaultdict(int)
        for v in self.lista:
            try:
                fecha = datetime.strptime(v[0], "%d/%m/%Y")
                mes_anio = fecha.strftime("%Y-%m")
                conteo[mes_anio] += 1
            except ValueError:
                continue
        return dict(sorted(conteo.items()))

    def dia_mayor_actividad(self):
        conteo = Counter(v[0] for v in self.lista if v[0])
        return conteo.most_common(1)[0] if conteo else ("N/A", 0)



