import os
import pandas as pd

INPUT_FILE="PRE_04_limpieza/data/ventas.csv"
OUTPUT_FILE="PRE_04_limpieza/submission/ventas_limpio.csv"

SUPPLIER_REPLACEMENTS = {
    "Bancolombia S.A.":["BANCOLOMBIA S.A."],
    "Corona S.A.S.":["Corona SAS"],
    "Ecopetrol S.A.":["Ecopetrol  S.A."],
    "Google Colombia Ltda.":["GOOGLE COLOMBIA LTDA."],
    "Microsoft Colombia Inc.":["MICROSOFT COLOMBIA INC."],
    "Postobon S.A.":["POSTOBON S.A.","POSTOBÓN S.A."],
    "SAP Colombia S.A.S.":["SAP Colombia S.A.S"],
    "Grupo Éxito S.A.":["GRUPO ÉXITO S.A.","Grupo  Éxito  S.A."],
    "SAP Colombia S.A.S.":["SAP Colombia SAS"],
    "Schneider Electric":["Schneider  Electric"],
    "Siemens S.A.S.":["SIEMENS S.A.S.","siemens s.a.s."],
    "Sura S.A.":["Sura  S.A."],
    "Telefónica Colombia":["Telefónica  Colombia"],
    "Nutresa S.A.":["NUTRESA S.A.","nutresa s.a.","Nutresa SA"],
    "Amazon Web Services Colombia":["amazon web services colombia"],
    "Cementos Argos S.A.":["Cementos Argos SA","cementos argos s.a."],
    "IBM Colombia S.A.S.":["IBM Colombia SAS.","ibm colombia s.a.s."],
    "Oracle Colombia Ltda.":["oracle colombia ltda","oracle colombia ltda.","Oracle Colombia",]
}

COUNTRY_REPLACEMENTS = {
    "Colombia":["CO","COL","COLOMBIA","Colombia","colombia"]
}

CITY_REPLACEMENTS = {"Medellín":["MEDELLÍN"," Medellin"," Medellín","medellín","Medellin"],
                     "Bogotá":["BOGOTÁ","bogotá"]

}

def make_replacements(series, replacements):
    for replacement, values in replacements.items():
        for value in values:
            series = series.replace(value, replacement)
    return series

def strip_whitespace(series):
    return series.str.strip()

def to_lowercase(series):
    return series.str.lower()

def replace_spaces_with_underscores(series):
    return series.str.replace(" ", "_")

def transform_dd_dd_dd_to_dd_dd_20dd(series):
    series = series.str.replace(r"^(\d{2})-(\d{2})-(\d{2})$", r"\1-\2-20\3", regex=True)
    return series

def transform_dd_mm_yyyy_to_yyyy_mm_dd(series):
    series = series.str.replace(r"^(\d{2})-(\d{2})-(\d{4})$", r"\3-\2-\1", regex=True)
    return series

def transform_yyyy_dd_mm_to_yyyy_mm_dd(series):

    def f(date):
        parts = date.split("-")
        if int(parts[1]) > 12:
            return f"{parts[0]}-{parts[2]}-{parts[1]}"
        return date

    series = series.apply(f)
    return series

def remove_k_in_amount(x):
    if isinstance(x, str) and x.endswith("K"):
        x=x[:-1]
        x=float(x)
        x*=1000
    return x

def remove_COP_in_amount(x):
    if isinstance(x, str) and x.startswith("COP"):
        x=x[3:]
        x=x.strip()
        x=x.replace(",","")
        x=float(x)
    return x

def remove_currency_in_amount(x):
    if isinstance(x, str) and x.startswith("$"):
        x=x[1:]
        x=x.strip()
        x=x.replace(",","")
        x=float(x)
    return x

def remove_point_in_amount(x):
    if isinstance(x, str) and x.endswith(".0"):
        x=x[:-2]
    if isinstance(x, str) and "." in x:
        x=x.replace(".","")
        x=float(x)
    return x

def remove_percent_in_discount(x):
    if isinstance(x, str) and x.endswith("%"):
        x=x[:-1]
        x=x.strip()
        x=float(x)
        x/=100
    return x
def transform_percent_to_decimal(x):
    if isinstance(x, str) and float(x) > 1:
        pass
    return x

def clean_column_names(df):
    df.columns = strip_whitespace(df.columns)
    df.columns = to_lowercase(df.columns)
    df.columns = replace_spaces_with_underscores(df.columns)
    return df

def clean_supplier_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, SUPPLIER_REPLACEMENTS)
    return series

def clean_country_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, COUNTRY_REPLACEMENTS)
    return series

def clean_city_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, CITY_REPLACEMENTS)
    return series

def clean_purchase_date_column(series):
    series = strip_whitespace(series)
    series = series.str.replace(r".", "-", regex=False)
    series = series.str.replace(r"/", "-", regex=False)
    series = transform_dd_dd_dd_to_dd_dd_20dd(series)
    series = transform_dd_mm_yyyy_to_yyyy_mm_dd(series)
    series = transform_yyyy_dd_mm_to_yyyy_mm_dd(series)
    return series

def clean_amount_column(series):
    series = strip_whitespace(series)
    series=series.apply(remove_k_in_amount)
    series=series.apply(remove_COP_in_amount)
    series=series.apply(remove_currency_in_amount)
    series=series.apply(remove_point_in_amount)
    return series

def clean_discount_column(series):
    series = strip_whitespace(series)
    series=series.apply(remove_percent_in_discount)
    return series

def main():
    df=pd.read_csv(INPUT_FILE)
    df = clean_column_names(df)
    df["supplier"] = clean_supplier_column(df["supplier"])
    df["country"] = clean_country_column(df["country"])
    df["city"] = clean_city_column(df["city"])
    df["purchase_date"] = clean_purchase_date_column(df["purchase_date"])
    df["amount"] = clean_amount_column(df["amount"])
    df["discount"] = clean_discount_column(df["discount"])
    df.to_csv(OUTPUT_FILE, index=False)

   

if __name__=="__main__":
    main()



