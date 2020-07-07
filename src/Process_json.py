# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

import logging
import json
from src.S3_Client import S3

import os
from itertools import chain


class ProcessJson(S3):

    _file_path = None       # type: str
    _raw_data = None        # type: dict
    _continents = []      # type: list()
    _keys = []              # type: list()

    def __init__(self) -> None:
        super(ProcessJson).__init__()

        print("Class Process Json Initialization ")

    def process_challenge(self):
        self._set_bucket()
        self._set_key_remove()
        self._set_file_path()
        self._read_json()
        self._iterate_json()
        self._process_json()

    def _read_json(self) -> None:
        with open(self._file_path) as f_in:
            data = json.load(f_in)

        if data:
            self._raw_data = data

    def _iterate_json(self) -> None:
        tmp = {}
        data = []

        for key, value in self._raw_data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, list):
                        for record in v:
                            self.delete_key(record)
                    tmp[k] = v
            tmp_2 = tmp.copy()
            data.append(tmp_2)
            self._set_continents(value)

        if data:
            self._raw_data = data

    def _set_continents(self, data) -> None:
        tmp = data.get("continent", None)

        if tmp not in self._continents and tmp is not None:
            self._continents.append(tmp)

    def delete_key(self, data) -> None:

        a = self._key_remove
        if self._key_remove in data:
            data.pop(self._key_remove)

    def _process_json(self) -> None:
        data = []
        for continent in self._continents:
            for count, row in enumerate(self._raw_data):
                if continent in row["continent"]:
                    data.append(row)

            file = self.write_data(continent, data)
            key = f"{continent}.json"
            self._upload_file_to_s3(file, key)
            data.clear()

    @staticmethod
    def write_data(file_name, data) -> str:

        path = os.path.join(os.getcwd(), "Test", "Results")
        file_name = f"{path}\{file_name}.json"
        data = json.dumps(data, indent=4)

        with open(file_name, 'w') as json_file:
            json_file.write(data)

        return file_name


