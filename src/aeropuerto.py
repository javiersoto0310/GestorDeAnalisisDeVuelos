class Aeropuerto:
    def __init__(self, vuelos: list):
        self.vuelos = vuelos
        self.aeropuertos = self._extraer_aeropuertos()

    def _extraer_aeropuertos(self):
        mapeo = {}
        for vuelo in self.vuelos:
            nombre_ciudad = vuelo[6].strip().upper()
            codigo = vuelo[5].strip().upper()
            if nombre_ciudad and codigo:
                mapeo[nombre_ciudad] = codigo
        return mapeo

    def obtener_ciudades_disponibles(self):
        return sorted(self.aeropuertos.keys())

    def obtener_codigo_iata(self, nombre_ciudad):
        return self.aeropuertos.get(nombre_ciudad.upper())
