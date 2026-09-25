import pandas as pd

INPUT_FILE="PRE_04_limpieza/data/ventas.csv"
OUTPUT_FILE="PRE_04_limpieza/submission/ventas_limpio.csv"

def main():
    df=pd.read_csv(OUTPUT_FILE)
    series = df["weight"]

    #series=series[series.str.contains(r"-",regex=False)]
    #series=series[series.str.contains(r"-d{2}$",regex=True)]
    #series = series.str.replace(r"\d", "d",regex=True)
    #series=series.astype(str)
    #series=series[series.str.startswith("$")]

    series = series.sort_values()

    series = series.drop_duplicates()
    

    print(series.head(25))
    print(f"Total unique amount: {len(series)}")

if __name__=="__main__":
    main()