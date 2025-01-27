import pandas as pd


class Definition:

    def __init__(self, database_path: str):
        self.data = pd.read_csv(database_path)

    def get(self, term: str):
        return tuple(self.data.loc[self.data["word"] == term]["definition"])