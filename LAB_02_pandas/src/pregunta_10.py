if __package__:
    from . import help
else:
    import help

def pregunta_10():
    """
    Usando `data/tbl0.tsv`, construya para cada categoría de la columna `c1`
    un texto con todos sus valores de la columna `c2`, ordenados de menor a
    mayor y separados por `:`. Retorne un DataFrame cuyo índice son las
    categorías, en orden alfabético, con una única columna llamada `c2`.

    Ejemplo del formato de la respuesta:

                           c2
        c1
        A     1:1:2:3:6:7:8:9
        B       1:3:4:5:6:8:9
        C           0:5:6:7:9
        ...
    """

    df= help.load_data("data/tbl0.tsv")
    col2=df.groupby("c1")["c2"]
    col2=col2.apply(lambda x: ":".join(map(str,sorted(x))))
    col2=col2.to_frame()
    result=col2.sort_index()
    return result