import gc
import os
import sys
from os.path import join

import dotenv
import pandas as pd


class Exercise:

    def __init__(self, env_path: str = join(os.path.dirname(__file__), '../.env')):
        self.data = None
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_to_dataframe(sep: str = ',', skip: int = 0) -> pd.DataFrame:
        path_file = os.getenv('CSV')
        return pd.read_csv(path_file, sep=sep, skiprows=skip)

    def replace_empty_values_on_file(self) -> pd.DataFrame:
        data = self.load_file_to_dataframe()
        data.fillna(value={
            'age': 0,
            'fare': 0,
            'cabin': 'unknown',
            'embarked': 'unknown', 'boat': 0, 'body': 0,
            'home.dest': 'unknown'
        }, inplace=True)
        return data

    def create_dummies(self, var_name: str = 'sex') -> pd.DataFrame:
        data = self.replace_empty_values_on_file()
        dummy = pd.get_dummies(data[var_name], prefix=var_name)
        data = data.drop(var_name, axis=1)
        data = pd.concat([data, dummy], axis=1)
        return data

    def save_data(self) -> None:
        data = self.create_dummies()
        path_save = os.getenv('SAVE')
        file_name = os.path.join(path_save, os.getenv('NAME_CSV'))
        print(data)
        return data.to_csv(file_name + '.csv', index=False)


if __name__ == "__main__":
    try:
        apply = Exercise()
        apply.save_data()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
