if __package__:
    from . import help
else:
    import help

def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """
    df=help.load_data()
    ans={}
    for line in df:
        values=line[4].split(",")
        for pair in values:
            value=pair.split(":")[0]
            if value in ans:
                ans[value]+=1
            else:
                ans[value]=1
    return ans
