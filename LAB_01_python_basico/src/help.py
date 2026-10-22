import gzip
from pathlib import Path

def load_data()-> list:
    """
    Carga los datos desde un archivo comprimido en formato gzip y devuelve
    una lista de listas, donde cada sublista representa una fila del archivo.

    """
    data_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"
    data = []
    with gzip.open(data_path, "rt", encoding="utf-8") as f:
        for line in f:
            line=line.replace("\n","")
            data.append(line.split("\t"))
    return data

def extract_month(date:str)->str:
    """
    Extrae el mes de una fecha en formato 'YYYY-MM-DD' y lo devuelve como
    un texto de dos dígitos.

    """
    month=date.split("-")[1]
    return month