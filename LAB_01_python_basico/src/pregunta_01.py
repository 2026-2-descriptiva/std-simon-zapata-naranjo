import LAB_01_python_basico.src.help as help

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """
    total = 0
    

    f=help.load_data()
    
    for line in f:
        total+=int(line[1])
            

    return total