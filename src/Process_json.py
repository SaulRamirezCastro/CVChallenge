# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

import logging
import json
from src.S3_Client import S3
from itertools import chain


class ProcessJson(S3):

    _file_path = None         #type: str
    _raw_data = None          #type: dict

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
        for k, v in self._raw_data.items():
            if isinstance(v, dict):
                for k_2, v_2 in v.items():
                    if isinstance(v_2, list):
                        for a in v_2:
                            self.delate_key(a)



                    tmp[k_2] = v_2
            tmp_2 = tmp.copy()
            data.append(tmp_2)
        if data:
            self._raw_data = data
    @staticmethod
    def delate_key(data) -> None:

        if "stringency_index" in data:
            data.pop("stringency_index")



