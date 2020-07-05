# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

from src.Process_json import ProcessJson


def test_init_class():
    process = ProcessJson()
    return process

def test_read_json():
    process = test_init_class()
    process._file_path = "D:/Users/SaulRC/PycharmProjects/CVChallenge/Test/Sample/dataset_covid.json"
    process.read_json()
    process.process_file()
    print(process._raw_data)
