import os
import gc
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv


def read_xls(env):
    """
    Dado un archivo XLS, se carga en un data frame
    :param env: Ubicacion dinamica del archivo de entrada
    :return: Dataframe
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    route = os.getenv('XLS')
    data = pd.read_excel(route).to_string()
    print(data)


if __name__ == "__main__":
    try:
        read_xls('.env')
        gc.enable()
    except KeyboardInterrupt:
        exit()
