import re
import pandas as pd

def pregunta_01():
  """
    El archivo `data/clusters_report.txt` es un reporte de clústeres de
    palabras clave pensado para ser leído por una persona, no por un programa:
    los encabezados ocupan varias líneas, las columnas están alineadas con
    espacios y la lista de palabras clave de un clúster continúa en las líneas
    siguientes.

    Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
    por clúster y las columnas:

    - `cluster`: número del clúster, como entero.
    - `cantidad_de_palabras_clave`: como entero.
    - `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
      texto `15,9 %` debe quedar como `15.9`.
    - `principales_palabras_clave`: todas las palabras clave del clúster en un
      solo texto, separadas por una coma y un único espacio.

    Retorne el DataFrame.

    Ejemplo del formato de la respuesta (se omite la última columna):

           cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
        0        1                         105                          15.9
        1        2                         102                          15.4
        ...
  """
  with open("data/clusters_report.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()

    clusters = []
    current_cluster = None

    for line in lines:
        line_str = line.strip()

        # Omitir encabezados y líneas separadoras
        if not line_str or line_str.startswith("-") or line_str.startswith("Cluster"):
            continue

        # Detectar el inicio de un clúster (comienza con números)
        match = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)$", line)

        if match:
            if current_cluster:
                clusters.append(current_cluster)

            current_cluster = {
                "cluster": int(match.group(1)),
                "cantidad_de_palabras_clave": int(match.group(2)),
                "porcentaje_de_palabras_clave": float(match.group(3).replace(",", ".")),
                "palabras": [match.group(4).strip()],
            }
        elif current_cluster:
            # Líneas subsecuentes de palabras clave del clúster actual
            current_cluster["palabras"].append(line_str)

    if current_cluster:
        clusters.append(current_cluster)

    # Formatear la columna de palabras clave
    for item in clusters:
        full_text = " ".join(item["palabras"])
        full_text = re.sub(r"\s+", " ", full_text)
        if full_text.endswith("."):
            full_text = full_text[:-1]
        item["principales_palabras_clave"] = full_text
        del item["palabras"]

    return pd.DataFrame(clusters)
