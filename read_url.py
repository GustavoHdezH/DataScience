import gc
import os
import sys

import urllib3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv


def get_url(env, head):
    """
    Encargada de optener datos de una url
    :param env: Archivo de configuracion
    :param head: Numero de filas a mostrar
    :return: Muestra de archivo procesado
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    route = os.getenv('URL')
    medals = pd.read_csv(route)
    print(medals.head(head).to_string())


def get_file_from_url(env, sep, head):
    """
    Encargada de optener informarcion y procesarla a un formato selecionado
    :param env: Archivo de configuracion
    :param head: Numero de filas a mostrar
    :param sep: Separador seleccionado
    :return: Archivo ya procesado en (xls, json, csv)
    """
    dotenv_path = Path(env)
    load_dotenv(dotenv_path)
    url = os.getenv('MEDALS')
    code = os.getenv('CODE')
    download = os.getenv('DOWNLOAD')
    filename = os.getenv('FILENAME')
    http = urllib3.PoolManager()
    request = http.request('GET', url)
    response = request.data
    if request.status == 200:
        # El objeto response contiene un string binario
        data = response.decode(code)
        # Se divide el string en un array de filas, separando por intros
        lines = data.split('\n')
        # se extrae la cabecera de la primera linea
        cols = lines[0].split(sep)
        n_cols = len(cols)
        # Se generar un dic vacio para llenarlo de la info procesada de la url
        counter = 0
        main_dict = {}
        for col in cols:
            main_dict[col] = []
        # Se procesa fila a fila la informacion para llenar el dic
        for line in lines:
            # Se salta la cabecera
            if counter > 0:
                # Se divide cada string por el separador seleccionado
                values = line.strip().split(sep)
                # Se agrega cada valor a su respectiva col del dic
                for i in range(len(cols)):
                    main_dict[cols[i]].append(values[i])
            counter += 1
        print('El data set tiene {} filas y {} columnas'.format(counter, n_cols))
        # Se conviertte el dic procesado a un df y se compruebna los valores
        df = pd.DataFrame(main_dict)
        print(df.head(head).to_string())
        df.to_csv(os.path.join(download, filename))
        print('Archivo guardado en: {}'.format(download))
    else:
        print("No hay conexión al servidor")
    return


if __name__ == "__main__":
    try:
        get_file_from_url('.env', ',', 5)
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
