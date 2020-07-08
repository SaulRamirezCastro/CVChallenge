# -*- coding: utf-8 -*-
# Created by SaulRC at 04/07/2020

from src.Process_json import ProcessJson


def test_init_class():
    process = ProcessJson()
    return process


def test_full_process():
    process = ProcessJson()
    process.process_challenge()
