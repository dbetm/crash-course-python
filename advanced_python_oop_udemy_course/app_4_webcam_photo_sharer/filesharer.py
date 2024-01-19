import os

from filestack import Client


class FileSharer:
    def __init__(self, filepath: str, api_key: str):
        self.filepath = filepath
        self.api_key = api_key

    def share(self) -> str:
        client = Client(self.api_key)
        # new_filelink = client.upload(filepath=self.filepath)
        # bacause filestack requires credit / debit card, then we will simulate the generation
        # which will be the local url to open in browser
        script_path = os.path.abspath(__file__)

        return f"{os.path.dirname(script_path)}/{self.filepath}"