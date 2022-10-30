import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv


def read_csv(env, sep, head):
    """
    Dado un archivo CSV, se carga en un data frame
    :param env: Ubicacion dinamica del archivo de entrada
    :param sep: separador designado para el archivo
    :param head: numero de filas a mostrar
    :return: Dataframe
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    route = os.getenv('CSV')
    data = pd.read_csv(route, sep=sep)
    print(data.head(head).to_string())
    rows = len(data.axes[0])
    cols = len(data.axes[1])
    print('Total rows: {}, and total cols: {}'.format(rows, cols))


if __name__ == "__main__":
    try:
        read_csv('.env', ',', 20)
    except KeyboardInterrupt:
        exit()
