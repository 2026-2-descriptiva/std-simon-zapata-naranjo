if __package__:
    from . import help
else:
    import help

def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """
    df=help.load_data()
    ans={}
    for line in df:
        value=int(line[1])
        letter=line[0]
        if value in ans:
            ans[value].append(letter)
        else:
            ans[value]=[letter]
    ans=[(value,ans[value]) for value in sorted(ans.keys())]
        
    return ans
