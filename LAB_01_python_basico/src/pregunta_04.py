if __package__:
    from . import help
else:
    import help

def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """
    df=help.load_data()
    ans_dic={}
    for line in df:
        month=help.extract_month(line[2])
        if month in ans_dic:
            ans_dic[month]+=1
        else:
            ans_dic[month]=1
    ans=[(key,ans_dic[key]) for key in sorted(ans_dic.keys())]
    return ans
