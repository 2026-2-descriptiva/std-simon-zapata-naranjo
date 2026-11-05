if __package__:
    from . import help
else:
    import help

def pregunta_01():
    """
    ¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        40
    """
    df=help.load_data("data/tbl0.tsv")
    return df.shape[0]
    
