if __package__:
    from . import help
else:
    import help

def pregunta_02():
    """
    ¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        4
    """
    df=help.load_data("data/tbl0.tsv")
    return df.shape[1]
    
