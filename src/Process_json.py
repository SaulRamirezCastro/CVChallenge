# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

import logging
import json
from src.S3_Client import S3
from itertools import chain


class ProcessJson(S3):

    _file_path = None         #type: str
    _raw_data = None          #type: dict
    _continet = None          #type: list()

    def __init__(self) -> None:
        super(ProcessJson).__init__()
        print("Class Process Json Initialization ")

    def read_json(self) -> None:

        with open(self._file_path) as f_in:
            data = json.load(f_in)

        if data:
            self._raw_data = data

    def iterate_json(self):
        pass

    def process_file(self):

        tmp = {}
        data = []
        continet = []

        for k, v in self._raw_data.items():
            if isinstance(v, dict):
                for k_2, v_2 in v.items():
                    if isinstance(v_2, list):
                        for a in v_2:
                            self.delate_key(a)
                    tmp[k_2] = v_2
            tmp_2 = tmp.copy()
            data.append(tmp_2)
            tmp_continet = v.get("continent", None)

            if tmp_continet not in continet and tmp_continet is not None:
                continet.append(tmp_continet)
        if data:
            self._raw_data = data
        if continet:
            self._continet = continet


    @staticmethod
    def delate_key(data) -> None:

        if "stringency_index" in data:
            data.pop("stringency_index")


    def separe_json(self):

        data =[]
        for continet in self._continet:
            for count, row in enumerate(self._raw_data):
                if continet in row["continent"]:
                    data.append(row)
                    #self._raw_data.pop(row)

            self.write_data(continet, data)
            data = []

    def write_data(self, file_name, data):

        file_name = f"{file_name}.json"
        data = json.dumps(data, indent=3)
        print(data)

        with open(file_name, 'w') as json_file:
            json_file.write(data)


