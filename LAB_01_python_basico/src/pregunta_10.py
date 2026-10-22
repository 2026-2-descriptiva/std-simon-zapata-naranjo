if __package__:
    from . import help
else:
    import help

def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo del formato de la respuesta:

        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """
    df=help.load_data()
    ans=[]
    for line in df:
        letter=line[0]
        code=len(line[3].split(","))
        metric=len(line[4].split(","))
        ans.append((letter,code,metric))
    return ans
