if __package__:
    from . import help
else:
    import help

def pregunta_06():
    """
    Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
    conviértalos a mayúsculas y retórnelos como una lista ordenada
    alfabéticamente.

    Ejemplo del formato de la respuesta:

        ["A", "B", "C", "D", "E", "F", "G"]
    """

    df=help.load_data("data/tbl1.tsv")
    return sorted(df["c4"].str.upper().unique().tolist())
