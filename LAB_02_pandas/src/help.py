import pandas as pd

def load_data(file_path)->pd.DataFrame:
    """
    Load tabular data from a tab-separated values (TSV) file.

    Parameters
    ----------
    file_path : str or path-like
        Path to the TSV file to load.

    Returns
    -------
    pandas.DataFrame
        The data read from the file using ``sep="\t"``.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    pandas.errors.ParserError
        If the file cannot be parsed as a delimited table.
    OSError
        If the file cannot be opened or read.
    """
    df=pd.read_csv(file_path,sep="\t")

    return df
