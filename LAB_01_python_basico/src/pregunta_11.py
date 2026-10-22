if __package__:
    from . import help
else:
    import help

def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"a": 122, "b": 49, "c": 91, ...}
    """
    df=help.load_data()
    ans={}
    for line in df:
        value=int(line[1])
        letters=line[3].split(",")
        for letter in letters:
            if letter in ans:
                ans[letter]+=value
            else:
                ans[letter]=value

    return ans
