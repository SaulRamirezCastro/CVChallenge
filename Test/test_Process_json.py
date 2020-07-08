# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

from src.Process_json import ProcessJson


def test_init_class():
    process = ProcessJson()
    return process

# def test_read_json():
#     process = test_init_class()
#     process._set_bucket()
#     process._set_key_remove()
#     process._set_file_path()
#     process._read_json()
#     process._iterate_json()
#     process._process_json()
#
#
#
#
# def test_set_bucket():
#     process = test_init_class()
#     process._set_file_path()
#     print(process._file_path)
#

def test_process():
    process = ProcessJson()
    process.process_challenge()
