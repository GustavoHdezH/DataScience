import gc
import os
import sys
from os.path import join

import dotenv
import pandas as pd
import urllib3


class ReadUrl:

    def __init__(self, env_path: str = join(os.path.dirname(__file__), '../.env')):
        """
        Initializes the class by loading environment variables.
        :param env_path: (Path, optional): Path to the environment file.
        """
        self.env_path = env_path
        dotenv.load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def extract_data_from_url() -> pd.DataFrame:
        """
        Download data from the specific URL and return it as a pd.DataFrame
        :return: pd.Dataframe: The downloaded data as dataframe
        """
        csv_from_url = os.getenv('URL')
        make_request = urllib3.request('GET', csv_from_url)
        return make_request.data.decode('utf-8')

    def transform_data_from_url(self) -> pd.DataFrame:
        data = self.extract_data_from_url()
        lines = data.split('\n')
        headers = lines[0].split(',')[:12]
        df = pd.DataFrame.from_records(
            [line.strip().split(',')[:12] for line in lines[1:]],
            columns=headers
        )
        df.fillna(0, inplace=True)
        return df

    def download_data_from_url(self):
        df = self.transform_data_from_url()
        path_download = os.getenv('DOWNLOAD')
        file_name = os.path.join(path_download, os.getenv('NAME'))
        df.to_csv(file_name + '.csv', index=False)


if __name__ == "__main__":
    try:
        reader = ReadUrl()
        reader.download_data_from_url()
        gc.enable()
    except KeyboardInterrupt:
        sys.exit()
