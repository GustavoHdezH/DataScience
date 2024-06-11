import os
import gc
import sys

import pandas as pd
from pathlib import Path
from dotenv import load_dotenv


class ReadFile:

    @staticmethod
    def load_dotenv(env: Path):
        load_dotenv(dotenv_path=env)

    @staticmethod
    def __configure_file_path() -> tuple:
        return (
            os.getenv('CSV')
        )

    @staticmethod
    def load_file_to_dataframe(sep, skip):
        path_file = ReadFile.__configure_file_path()
        data = pd.read_csv(path_file, sep=sep, skiprows=skip)
        return data

    @staticmethod
    def show_info(sep, rows):
        data = ReadFile.load_file_to_dataframe(sep, rows)
        print(data.head(rows).to_string())
        row = len(data.axes[0])
        cols = len(data.axes[1])
        print('Total rows: {}, and total cols: {}'.format(row, cols))


if __name__ == "__main__":
    try:
        ReadFile.load_dotenv('.env')
        ReadFile.show_info(',', 50)
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
