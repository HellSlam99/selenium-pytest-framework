import pandas as pd


class CSVReader:

    @staticmethod
    def read(file_path):

        dataframe = pd.read_csv(file_path)

        return dataframe.to_dict(orient="records")