if __package__:
    from . import help
else:
    import help

def pregunta_13():
    """
    Combine las tablas `data/tbl0.tsv` y `data/tbl2.tsv` usando la columna
    `c0`, que ambas comparten. Luego, sume los valores de la columna `c5b`
    para cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo
    índice son las categorías, en orden alfabético, y cuyos valores son las
    sumas.

    Ejemplo del formato de la respuesta:

        c1
        A    146
        B    134
        C     81
        ...
    """

    df0=help.load_data("data/tbl0.tsv")
    df2=help.load_data("data/tbl2.tsv")
    merged_df=df0.merge(df2, on="c0")
    result=merged_df.groupby("c1")["c5b"].sum()
    result=result.sort_index()
    return result
