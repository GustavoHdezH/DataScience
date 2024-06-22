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
        # Counting all values
        headers = data.columns
        empty_values_by_column = {}
        for header in headers:
            empty_values_in_column = pd.isnull(data[header]).values.sum()
            empty_values_by_column[header] = empty_values_in_column
        for header, empty_value_count in empty_values_by_column.items():
            print(f"Empty values in '{header}': {empty_value_count}")
        # Example for counting individual values
        print("Empty body values: {}".format(pd.isnull(data["home.dest"]).values.ravel().sum()))

    def replace_empty_values_on_file(self):
        data = self.load_file_to_dataframe()
        replace_values = {
            "age": 0,
            "fare": 0,
            "cabin": "unknown",
            "embarked": "unknown",
            "boat": 0,
            "body": 0,
            "home.dest": "unknown"
        }
        data = data.fillna(replace_values)
        return data

    def save_data(self):
        data = self.replace_empty_values_on_file()
        path_save = os.getenv('SAVE')
        file_name = os.path.join(path_save, os.getenv('NAME_CSV'))
        return data.to_csv(file_name + '.csv', index=False)


if __name__ == "__main__":
    try:
        reader = ReplaceValues()
        reader.save_data()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
