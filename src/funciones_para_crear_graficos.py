import matplotlib.pyplot as plt
import os

def graficar_clases_vuelo(resultados, ciudad_elegida):
    tipos = [r[0] for r in resultados]
    cantidades = [r[1] for r in resultados]

    plt.figure(figsize=(8, 5))
    plt.bar(tipos, cantidades, color='skyblue')
    plt.title(f"Tipos de vuelo en {ciudad_elegida.title()}")
    plt.xlabel("Tipo de vuelo")
    plt.ylabel("Cantidad de vuelos")
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs("graficos", exist_ok=True)
    nombre_imagen = f"graficos/grafico_clases_vuelo_{ciudad_elegida.lower().replace(' ', '_')}.png"
    plt.savefig(nombre_imagen)
    print(f"\nGráfico guardado como '{nombre_imagen}'")


def graficar_pasajeros(abordaron, descendieron, ciudad_elegida):
    etiquetas = ["Abordaron", "Descendieron"]
    valores = [abordaron, descendieron]
    colores = ["#66b3ff", "#99ff99"]

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90, colors=colores)
    plt.title(f"Distribución de pasajeros en {ciudad_elegida.title()}")
    plt.axis("equal")

    os.makedirs("graficos", exist_ok=True)
    nombre_imagen = f"graficos/pasajeros_torta_{ciudad_elegida.lower().replace(' ', '_')}.png"
    plt.savefig(nombre_imagen)
    print(f"\nGráfico guardado como '{nombre_imagen}'")
