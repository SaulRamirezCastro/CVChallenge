# -*- coding: utf-8 -*-
# Created by SaulRC at 03/07/2020

import logging
import os

import boto3
from botocore.exceptions import ClientError

from src.config import config as cf


class S3:
    """"Class to get Aws S3 connection

    """

    _bucket = None              # type: str
    _file_path = None           # type: str
    _key_remove = None          # type: str

    def __init__(self) -> None:
        """"Initialisation of the class S3.

        Return:
            None
        """

        logging.info("Aws S3 client Initialisation ")

    def _set_key_remove(self) -> None:
        """"Set the class variable _key_remove with teh data from teh config file

        Return:
            None
        """
        if self._key_remove is None:
            self._key_remove = cf.key_remove

    def _set_bucket(self) -> None:
        """set the class variable _bucket with teh data from teh config file

        Return:
            None
        """
        if self._bucket is None:
            self._bucket = cf.bucket

    def _set_file_path(self) -> None:
        """

        """
        sample_path = os.path.join(os.getcwd(), "Test", "Sample")
        file_name = f"{sample_path}\{cf.file_name}"
        if os.path.exists(file_name):
            self._file_path = file_name
        else:
            logging.info(f"File {file_name} doesn’t   exist ")

    @property
    def _s3_client(self) -> boto3.client:
        """Get S3 connection.

        Return:
            S3 connection
        """
        return boto3.client('s3')

    def _upload_file_to_s3(self, source_path: str, key: str) -> bool:
        """Upload the file to S3 bucket
        Argument:
            source_path(str): Path from the file
            key(str): Key name

        Return:
            bool
        """
        try:
            self._s3_client.upload_file(source_path, self._bucket, key)
        except ClientError as e:
            logging.exception(e)

        return True
