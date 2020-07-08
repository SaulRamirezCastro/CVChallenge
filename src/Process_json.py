# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

import json
import os

from src.S3_Client import S3


class ProcessJson(S3):
    """""Class to process the Json file, remove one key and split by country

    Method:
        process_challenge
    """

    # Class Variable

    _file_path = None       # type: str
    _raw_data = None        # type: dict
    _continents = []        # type: list()
    _keys = []              # type: list()

    def __init__(self) -> None:
        """"Initialice the class ProcessJson and super Class S3
        """
        print("Class Process Json Initialization ")
        super(ProcessJson).__init__()

    def process_challenge(self) -> None:
        """Method execute all the process

        Returm:
            None
        """
        self._set_bucket()
        self._set_key_remove()
        self._set_file_path()
        self._read_json()
        self._iterate_json()
        self._process_json()

    def _read_json(self) -> None:
        """Read json file and set teh raw data in class variable _raw_data

        Return:
            None
        """
        with open(self._file_path) as f_in:
            data = json.load(f_in)

        if data:
            self._raw_data = data

    def _iterate_json(self) -> None:
        """Iterate the Json data in teh class variable _raw_data

        Return:
            None
        """
        tmp = {}
        data = []

        for key, value in self._raw_data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, list):
                        for record in v:
                            self._delete_key(record)
                    tmp[k] = v
            tmp_2 = tmp.copy()
            data.append(tmp_2)
            self._set_continents(value)
            tmp.clear()

        if data:
            self._raw_data = data

    def _set_continents(self, data: dict) -> None:
        """Get the continents from the json data  and set in the class variable __continents
        Argument:
            data(dict) :  A dictionary that contains the key continent

        Return:
            None
        """
        tmp = data.get("continent", None)

        if tmp not in self._continents and tmp is not None:
            self._continents.append(tmp)

    def _delete_key(self, data) -> None:
        """Delete the key store in class variable _key_remove and delete from data as dictionary
        Argument:
            data(dict) :  data as dict

        Return:
            None
        """
        if self._key_remove in data:
            data.pop(self._key_remove)

    def _process_json(self) -> None:
        """Generate the json file per continent

        Return:
            None
        """
        data = []
        for continent in self._continents:
            for count, row in enumerate(self._raw_data):
                json_continent = row.get("continent", None)
                if continent == json_continent:
                    data.append(row)

            file = self.write_data(continent, data)
            key = f"{continent}.json"
            self._upload_file_to_s3(file, key)
            data.clear()

    @staticmethod
    def write_data(file_name: str, data: dict) -> str:
        """Write the data as json file.
        Argument:
            file_name(str): Name of the file
            data(dict): data as dict

        Return:
            file_name(str): Path from the file
        """
        path = os.path.join(os.getcwd(), "Test", "Results")
        file_name = f"{path}\{file_name}.json"
        data = json.dumps(data, indent=4)

        with open(file_name, 'w') as json_file:
            json_file.write(data)

        return file_name
