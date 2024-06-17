import gc
import os
import sys
from pathlib import Path

import dotenv
import pandas as pd


class ReplaceValues:

    def __init__(self, env_path: Path = Path('../.env')):
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_to_dataframe(sep: str = ',', skip: int = 0) -> pd.DataFrame:
        path_file = os.getenv('CSV')
        return pd.read_csv(path_file, sep=sep, skiprows=skip)

    def show_value_type(self) -> type:
        data = self.load_file_to_dataframe()
        return data.dtypes

    def describe_dataframe(self):
        data = self.load_file_to_dataframe()
        return data.describe()

    def show_empty_values_on_file(self) -> None:
        data = self.load_file_to_dataframe()
        print("Empty age values: {}".format(pd.isnull(data["age"]).values.ravel().sum()))
        print("Empty fare values: {}".format(pd.isnull(data["fare"]).values.ravel().sum()))
        print("Empty cabin values: {}".format(pd.isnull(data["cabin"]).values.ravel().sum()))
        print("Empty embarked values: {}".format(pd.isnull(data["embarked"]).values.ravel().sum()))
        print("Empty boat values: {}".format(pd.isnull(data["boat"]).values.ravel().sum()))
        print("Empty body values: {}".format(pd.isnull(data["body"]).values.ravel().sum()))

    def replace_empty_values_on_file(self):
        data = self.load_file_to_dataframe()
        data["age"] = data["age"].fillna(0)
        data["fare"] = data["fare"].fillna(0)
        data["cabin"] = data["cabin"].fillna('unknown')
        data["embarked"] = data["embarked"].fillna('unknown')
        data["boat"] = data["boat"].fillna(0)
        data["body"] = data["body"].fillna(0)
        path_save = os.getenv('SAVE')
        file_name = os.path.join(path_save, os.getenv('NAME_CSV'))
        return data.to_csv(file_name + '.csv', index=False)


if __name__ == "__main__":
    try:
        reader = ReplaceValues()
        reader.replace_empty_values_on_file()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
