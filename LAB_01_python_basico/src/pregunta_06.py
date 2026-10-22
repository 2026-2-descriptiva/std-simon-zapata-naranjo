if __package__:
    from . import help
else:
    import help

def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """
    df=help.load_data()
    ans={}
    for line in df:
        pairs=line[4].split(",")
        for pair in pairs:
            key,value=pair.split(":")
            value=int(value)
            if key in ans:
                ans[key][0]=min(ans[key][0],value)
                ans[key][1]=max(ans[key][1],value)
            else:
                ans[key]=[value,value]
    ans=[(key,ans[key][0],ans[key][1]) for key in sorted(ans.keys())]
                                
    return ans
