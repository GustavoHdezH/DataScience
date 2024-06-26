import gc
import os
import sys
from pathlib import Path

import dotenv
import pandas as pd


class DummyData:

    def __init__(self, env_path: Path = Path('../.env')) -> dotenv:
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_to_dataframe(sep: str = ',', skip: int = 0) -> pd.DataFrame:
        path_file = os.getenv('CSV')
        return pd.read_csv(path_file, sep=sep, skiprows=skip)

    def dummy_variable(self) -> pd.get_dummies:
        data = self.load_file_to_dataframe()
        dummy_gender = pd.get_dummies(data["sex"], prefix="sex")
        return dummy_gender

    def drop_dummy_column(self):
        data = self.load_file_to_dataframe()
        drop_column = data.drop(['sex'], axis=1)
        return drop_column

    def concat_dummy_variable_on_data(self):
        data = self.drop_dummy_column()
        gender = self.dummy_variable()
        data = pd.concat([data, gender], axis=1)
        return data.to_string()

    def create_dummies(self, var_name):
        data = self.load_file_to_dataframe()
        dummy = pd.get_dummies(data[var_name], prefix=var_name)
        data = data.drop(var_name, axis=1)
        data = pd.concat([data, dummy], axis=1)
        return print(data.to_string())


if __name__ == "__main__":
    try:
        reader = DummyData()
        reader.create_dummies('sex')
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
