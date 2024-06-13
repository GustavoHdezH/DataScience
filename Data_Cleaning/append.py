import os
import gc
import sys

import pandas as pd
from pathlib import Path
import dotenv


class Append:
    """
    This class facilitates appending data from a file with headers to another file with data.
    """
    def __init__(self, env_path: Path = Path('../.env')):
        """
        Initializes the class by loading environment variables.
        :param env_path: (Path, optional): Path to the environment file.
        """
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_with_headers():
        """
        Loads a file containing colum headers as a pandas DataFrame
        :return: pd.DataFrame: A DataFrame containing the loaded column headers
        """
        path_headers = os.getenv('HEADERS')
        return pd.read_csv(path_headers)

    def append_headers_and_data_in_file(self):
        """
        Appends data from a file to another file using columns headers
        :return:
        """
        path_file = os.getenv('TXT')
        headers = self.load_file_with_headers()["Column_Names"].tolist()
        data = pd.read_csv(path_file, header=None, names=headers)
        return print(data)


if __name__ == "__main__":
    try:
        reader = Append()
        reader.append_headers_and_data_in_file()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
