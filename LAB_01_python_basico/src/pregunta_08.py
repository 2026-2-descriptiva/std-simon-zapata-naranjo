if __package__:
    from . import help
else:
    import help

def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """
    df=help.load_data()
    ans={}
    for line in df:
        value=int(line[1])
        letter=line[0]
        if value in ans:
            if letter not in ans[value]:
                ans[value].add(letter)
        else:
            ans[value]=set([letter])
    ans=[(value,sorted(ans[value])) for value in sorted(ans.keys())]
        
    return ans
