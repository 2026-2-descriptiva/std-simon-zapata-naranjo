if __package__:
    from . import help
else:
    import help

def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """
    df=help.load_data()
    ans_dic={}

    for line in df:
        if line[0] in ans_dic:
            ans_dic[line[0]]+=int(line[1])
        else:
            ans_dic[line[0]]=int(line[1])
    ans=[(key,ans_dic[key]) for key in sorted(ans_dic.keys())]
    
    return ans
