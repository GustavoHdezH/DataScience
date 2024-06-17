import os
import gc
import sys

import pandas as pd
from pathlib import Path
import dotenv


class ReadXls:

    def __init__(self, env_path: Path = Path('../.env')):
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def load_file_to_dataframe() -> pd.DataFrame:
        path_file = os.getenv('XLSX')
        return pd.read_excel(path_file)

    def show_info_on_terminal(self) -> None:
        data = self.load_file_to_dataframe()
        print(data.head().to_string())


if __name__ == "__main__":
    try:
        reader = ReadXls()
        reader.show_info_on_terminal()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
