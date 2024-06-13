import os
import gc
import sys

import pandas as pd
from pathlib import Path
import dotenv


class ReadTxt:
    """
    A class for efficiently reading TXT files and display information.
    """

    def __init__(self, env_path: Path = Path('../.env')):
        """
        Initializes the class by loading environment variables.
        :param env_path: (Path, optional): Path to the environment file.
        """
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_to_dataframe(sep: str = ',', skip: int = 0) -> pd.DataFrame:
        """
        Loads a TXT file into pandas Dataframe
        :param sep: (str, optional): Column separator.
        :param skip: (int, optional):Number of rows to skip at the beginning.
        :return: pd.Dataframe
        """
        path_file = os.getenv('TXT')
        return pd.read_csv(path_file, sep=sep, skiprows=skip)

    def show_info_on_terminal(self, rows: int = 20) -> None:
        """
        Prints information about the loaded DataFrame
        :param rows: (int, optional): Number of rows to display from head.
        """
        data = self.load_file_to_dataframe()
        print(data.head(rows).to_string())
        print("Total rows: {}, and total cols: {}".format(len(data.index), len(data.columns)))


if __name__ == "__main__":
    try:
        reader = ReadTxt()
        reader.show_info_on_terminal()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
