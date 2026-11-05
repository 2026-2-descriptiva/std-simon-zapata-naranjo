import pandas as pd
import os

def pregunta_01():
    """
    Las frases de este laboratorio no están en una tabla, sino en miles de
    archivos de texto organizados en carpetas. Dentro de `data/` hay dos
    carpetas, `train/` y `test/`, y cada una contiene las carpetas
    `negative/`, `neutral/` y `positive/`. Cada archivo `.txt` contiene una
    frase, y la carpeta donde se encuentra indica su sentimiento.

    Su tarea es construir un dataset para cada división y guardarlo en:

    - `submission/train_dataset.csv`
    - `submission/test_dataset.csv`

    Cada archivo debe tener dos columnas: `phrase`, con el texto de la frase,
    y `target`, con el nombre de la carpeta de sentimiento (`negative`,
    `neutral` o `positive`). Recorra las carpetas y los archivos en orden
    alfabético, de modo que el resultado sea siempre el mismo. No guarde el
    índice de Pandas en el CSV.

    Ejemplo del formato de cada archivo:

        phrase,target
        "The real estate company posted a net loss ...",negative
        ...
        "Cardona slowed her vehicle , turned around ...",neutral
        ...
    """

    os.makedirs("submission", exist_ok=True)

    for split in ["train", "test"]:
        split_dir = os.path.join("data", split)
        records = []

        # Recorrer carpetas de sentimiento en orden alfabético
        targets = sorted(os.listdir(split_dir))
        for target in targets:
            target_dir = os.path.join(split_dir, target)
            if not os.path.isdir(target_dir):
                continue

            # Recorrer archivos .txt en orden alfabético
            filenames = sorted(os.listdir(target_dir))
            for filename in filenames:
                if filename.endswith(".txt"):
                    file_path = os.path.join(target_dir, filename)
                    with open(file_path, mode="r", encoding="utf-8") as f:
                        phrase = f.read().strip()
                    records.append({"phrase": phrase, "target": target})

        df = pd.DataFrame(records)
        df.to_csv(f"submission/{split}_dataset.csv", index=False)
