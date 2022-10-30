import os
import gc
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv


def columnas(env, sep):
    """
    Encargada de conocer las columnas de un archivo txt
    :param sep: Separador asignado
    :param env: ubicacion de archivo de entrada
    :return: Numero de columnas
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    route = os.getenv('TXT')
    with open(route, "r") as file:
        cols = file.readline().strip().split(sep)
        n_cols = len(cols)
        print("El numero de columnas son: {}".format(n_cols))
        file.close()


def filas(env, sep):
    """
    Encargada de conocer las filas de un archivo txt
    :param env: Ubicacion del archivo de conf
    :param sep: Separador asignado
    :return:
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    route = os.getenv('TXT')
    # Conteo de columnas
    with open(route, "r") as file:
        cols = file.readline().strip().split(sep)
        n_cols = len(cols)
        # Conteo de filas
        counter = 0
        main_dict = {}
        for col in cols:
            main_dict[col] = []
        for line in file:
            values = line.strip().split(sep)
            for i in range(len(cols)):
                main_dict[cols[i]].append(values[i])
            counter += 1
    print("El data set tiene: {} filas y {} columnas".format(counter, n_cols))


def conversion(env, sep):
    """conversion()
    Función encargada de conocer las columas y filas de un archivo y convertirlo a un Dataframe
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    route = os.getenv('TXT')
    with open(route, "r") as data_set:
        cols = data_set.readline().strip().split(sep)
        n_cols = len(cols)
        counter = 0
        main_dict = {}
        for col in cols:
            main_dict[col] = []
        for line in data_set:
            values = line.strip().split(",")
            for i in range(len(cols)):
                main_dict[cols[i]].append(values[i])
            counter += 1
    dataframe = pd.DataFrame(main_dict)
    df = dataframe.head(20).to_string()
    print(df)


if __name__ == "__main__":
    try:
        filas('.env', ',')
        conversion('.env', ',')
        gc.enable()
    except KeyboardInterrupt:
        exit()
