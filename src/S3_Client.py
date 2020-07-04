# -*- coding: utf-8 -*-
# Created by SaulRC at 03/07/2020

import logging

import boto3
from botocore.exceptions import ClientError


class S3:
    _s3_client = None  # type: boto3.client

    def __init__(self):
        logging.info("Aws S3 client Initialisation ")

    @property
    def _s3_client(self) -> boto3.client:

        try:
            if self._s3_client is None:
                self._s3_client = boto3.resource('s3')
        except ClientError as e:
            logging.exception(e)
        return self._s3_client

    def _upload_file_to_s3(self, source_path: str,bucket,s3_destination) -> bool:

        try:
            self._s3_client.upload_file(source_path, bucket, s3_destination)
        except ClientError as e:
            logging.exception(e)

        return True
