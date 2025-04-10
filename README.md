# Sistema de Análisis de Datos de Vuelos 2021

Este proyecto es una herramienta diseñada para analizar datos de vuelos registrados en el año 2021. Utiliza una base de datos obtenida del portal de datos abiertos de Argentina ([datos.gob.ar](https://www.datos.gob.ar)) y permite realizar consultas estadísticas y visualizaciones gráficas sobre los vuelos.

## Funcionalidades

El sistema proporciona las siguientes opciones de análisis:

1. **Información General del Año 2021**:
   - Cantidad total de vuelos registrados.
   - Desglose entre vuelos domésticos e internacionales.
   - Cantidad de aterrizajes y despegues.
   - Total de pasajeros transportados.

2. **Movimientos y Tipos de Vuelos por Ciudad y Rango de Fechas**:
   - Consulta de despegues, aterrizajes y clases de vuelos en una ciudad específica dentro de un rango de fechas.

3. **Cantidad de Pasajeros y Aerolíneas por Ciudad y Rango de Fechas**:
   - Total de pasajeros que abordaron y descendieron.
   - Lista de aerolíneas utilizadas en los vuelos.

4. **Ranking de Aerolíneas Más Usadas**:
   - Muestra las aerolíneas con mayor cantidad de vuelos realizados.

5. **Destinos Más Frecuentes desde un Aeropuerto**:
   - Identifica los principales destinos desde un aeropuerto específico.

6. **Estadísticas por Avión (Matrícula)**:
   - Listado de las matrículas de aeronaves con mayor cantidad de vuelos realizados.

7. **Vuelos por Mes**:
   - Cantidad de vuelos distribuidos mes a mes.

8. **Día de Mayor Actividad Aérea**:
   - Identificación del día con mayor cantidad de vuelos registrados.

## Dataset

La base de datos utilizada fue obtenida del portal [datos.gob.ar](https://www.datos.gob.ar) y contiene información detallada de los vuelos realizados durante el año 2021. Incluye datos como:
- Fecha y hora (UTC).
- Clase de vuelo.
- Tipo de movimiento (despegue o aterrizaje).
- Aeropuerto de origen/destino.
- Aerolínea.
- Matrícula del avión.
- Total de pasajeros.

## Requisitos

El proyecto utiliza la biblioteca `matplotlib` para generar gráficos, especificada en el archivo `requirements.in`. Asegúrate de instalar todas las dependencias antes de ejecutar el programa.

## Clonar el repositorio y ejecutar el sistema

Sigue estos pasos para configurar el entorno y ejecutar el sistema:

1. **Clonar el repositorio**
   - Abre una terminal y ejecuta el siguiente comando para clonar el repositorio del proyecto:
     ```bash
     git clone https://github.com/javiersoto0310/GestorDeAnalisisDeVuelos.git
     ```
     
2. **Navegar al directorio del proyecto**
   - Cambia al directorio donde se clonó el repositorio:
     ```bash
     cd GestorDeAnalisisDeVuelos
     ```

3. **Crear un entorno virtual**
   - Crea un entorno virtual utilizando `venv`:
     ```bash
     python -m venv .venv
     ```

4. **Activar el entorno virtual**
   - En sistemas **Linux/macOS**, ejecuta:
     ```bash
     source .venv/bin/activate
     ```
   - En sistemas **Windows**, ejecuta:
     ```bash
     .venv\Scripts\activate
     ```

5. **Instalar la herramienta `pip-tools`**
   - Dentro del entorno virtual, instala `pip-tools` para compilar el archivo `requirements.in`:
     ```bash
     pip install pip-tools
     ```

6. **Generar el archivo `requirements.txt`**
   - Compila el archivo `requirements.in` para generar `requirements.txt`:
     ```bash
     pip-compile requirements.in
     ```

7. **Instalar las dependencias**
   - Usa el archivo generado para instalar las dependencias:
     ```bash
     pip install -r requirements.txt
     ```

8. **Ejecutar el programa**
   - Inicia el programa ejecutando el archivo `main.py`:
     ```bash
     python src/main.py
     ```










