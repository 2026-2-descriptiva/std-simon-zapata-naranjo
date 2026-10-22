if __package__:
    from . import help
else:
    import help

def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """
    df=help.load_data()
    ans={}
    for line in df:
        l=line[0]
        v=int(line[1])
        if l in ans:
            ans[l][0]=max(ans[l][0],v)
            ans[l][1]=min(ans[l][1],v)
        else:
            ans[l]=[v,v]
    ans=[(key,ans[key][0],ans[key][1]) for key in sorted(ans.keys())]
        
    return ans
