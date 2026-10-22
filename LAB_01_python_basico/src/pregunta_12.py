if __package__:
    from . import help
else:
    import help

def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """
    df= help.load_data()
    ans={}
    for line in df:
        letter=line[0]
        metrics=line[4].split(",")
        s=0
        for metric in metrics:
            key,value=metric.split(":")
            s+=int(value)
        if letter in ans:
            ans[letter]+=s
        else:
            ans[letter]=s
    
    return ans
