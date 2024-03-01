import boto3
import botocore
import os
import logging
from botocore.exceptions import ClientError


class AWSBuckets:
    """
    Class to represent AWSBuckets objects
    -----
    Methods:
        create_bucket (bucket_name: str, region: str): creates s3 bucket with specific name and region
        create_folder (bucket_name: str, folder_name: str): creates folder in s3 bucket
        upload_file_to_bucket (bucket_name: str, folder_name: str, object_name: str): uploads file to the s3 bucket
        upload_file_to_folder (file_path: str, bucket_name: str, file_name: str): uploads file to specific folder in bucket
        download_s3_folder (bucket_name: str, s3_folder: str, local_dir: str): downloads folder form s3 bucket
        remove_csvs (bucket_name: str): deletes only csv files form s3 bucket
        empty_bucket (bucket_name: str): deletes everything from the bucket
    """

    def __init__(self):
        config = botocore.config.Config(
            read_timeout=900, connect_timeout=900, retries={"max_attempts": 5}
        )

        self.s3 = boto3.client("s3", config=config)
        self.s3_resource = boto3.resource("s3", config=config)

    def create_bucket(self, bucket_name: str, region: str = None):
        """
        Creates S3 bucket with provided name and region
        :param:
        bucket_name (str): specifies the bucket name
        region (sts): specifies the aws region to be used on bucket creation (important to match the region from SF account)
        :return:
            (bool): if bucket created successfully method returns True
        """
        try:
            if region is None:
                self.s3.create_bucket(Bucket=bucket_name)
            else:
                self.s3 = boto3.client("s3", region_name=region)
                location = {"LocationConstraint": region}
                self.s3.create_bucket(
                    Bucket=bucket_name, CreateBucketConfiguration=location
                )
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def create_folder(self, bucket_name: str, folder_name: str):
        """
        Creates folder in s3 bucket
        :param
            bucket_name (str): specifies the bucket to be used
            folder_name (str): specifies the folder name
        """
        self.s3.put_object(Bucket=bucket_name, Key=(folder_name + "/"))

    def upload_file_to_bucket(
        self, bucket_name: str, file_name: str, object_name: str = None
    ):
        """
        Uploads file to s3 bucket
        :param:
            bucket_name (str): specifies the bucket to upload to
            file_name (str): specifies the file to be uploaded
            object_name (str): S3 object name (default: None the file_name is used)
        :return:
            (bool): True if file was uploaded, else False
        """
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            self.s3.upload_file(file_name, bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def upload_file_to_folder(self, file_path: str, bucket_name: str, file_name: str):
        """
        Uploads specific file to s3 folder (object)
        :param:
         file_path (str): path the file to be loaded into s3 bucket
         bucket_name (str): name of the bucket to be used
         file_name (str): The name of the file to upload to.
        """
        self.s3_resource.meta.client.upload_file(file_path, bucket_name, file_name)

    def download_s3_folder(
        self, bucket_name: str, s3_folder: str, local_dir: str = None
    ):
        """
        Download the content of a folder directory in s3 bucket
        :param:
            bucket_name: the name of the s3 bucket
            s3_folder: the folder path in the s3 bucket to download from
            local_dir: a relative or absolute directory path to download to
        """
        bucket = self.s3_resource.Bucket(bucket_name)
        for obj in bucket.objects.filter(Prefix=s3_folder):
            target = (
                obj.key
                if local_dir is None
                else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
            )
            if not os.path.exists(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            if obj.key[-1] == "/":
                continue
            bucket.download_file(obj.key, target)

    def remove_csvs(self, bucket_name: str):
        """
        Deletes .csv files from a bucket
        :param:
            bucket_name (str): bucket name with content to be deleted
        :return:
            bool: True if content is deleted successfully, otherwise False
        """
        try:
            response = self.s3.list_objects(Bucket=bucket_name)
            if "Contents" in response:
                for item in response["Contents"]:
                    if item["Key"].endswith(".csv"):
                        print("deleting file", item["Key"])
                        self.s3.delete_object(Bucket=bucket_name, Key=item["Key"])
        except ValueError:
            print("Not possible to empty the bucket!")
            return False
        return True

    def empty_bucket(self, bucket_name: str):
        """
        Deletes all the files/folders from a bucket
        :param:
            bucket_name (str): bucket name with content to be deleted
        :return:
            bool: True if content is deleted successfully, otherwise False
        """
        try:
            response = self.s3.list_objects(Bucket=bucket_name)
            if "Contents" in response:
                for item in response["Contents"]:
                    print("deleting file", item["Key"])
                    self.s3.delete_object(Bucket=bucket_name, Key=item["Key"])
        except ValueError:
            print("Not possible to empty the bucket!")
            return False
        return True
