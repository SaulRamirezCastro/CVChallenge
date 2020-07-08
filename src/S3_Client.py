# -*- coding: utf-8 -*-
# Created by SaulRC at 03/07/2020

import logging

import boto3
from src.config import config as cf
import os
from botocore.exceptions import ClientError


class S3:

    _s3 = None            # type: boto3.client
    _bucket = None              # type: str
    _file_path = None           # type: str
    _key_remove = None          # type: str

    def __init__(self) -> None:
        logging.info("Aws S3 client Initialisation ")
        self._set_bucket()
        self._set_key_remove()
        self._set_file_path()

    def _set_key_remove(self):
        if self._key_remove is None:
            self._key_remove = cf.key_remove

    def _set_bucket(self):
        if self._bucket is None:
            self._bucket = cf.bucket

    def _set_file_path(self) -> None:
        sample_path = os.path.join(os.getcwd(), "Test", "Sample")
        file_name = f"{sample_path}\{cf.file_name}"
        if os.path.exists(file_name):
            self._file_path = file_name
        else:
            logging.info(f"File {file_name} doesn’t   exist ")

    @property
    def _s3_client(self) -> boto3.client:
        return boto3.client('s3')

    def _upload_file_to_s3(self, source_path: str, key: str) -> bool:

        try:
            self._s3_client.upload_file(source_path, self._bucket, key)
        except ClientError as e:
            logging.exception(e)

        return True
