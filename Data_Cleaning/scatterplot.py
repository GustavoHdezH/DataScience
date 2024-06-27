import gc
import os
import sys
from os.path import join

import dotenv
import pandas as pd


class Scatterplot:

    def __init__(self, env_path: str = join(os.path.dirname(__file__), '../.env')) -> dotenv:
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_to_dataframe(sep: str = ',', skip: int = 0) -> pd.DataFrame:
        path_file = os.getenv('TXT')
        return pd.read_csv(path_file, sep=sep, skiprows=skip)

    def scatterplot(self):
        data = self.load_file_to_dataframe()
        data.plot(kind="scatter", x="Day Mins", y="Day Charge")


if __name__ == "__main__":
    try:
        reader = Scatterplot()
        reader.scatterplot()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
