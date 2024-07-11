import os
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def process_data_function():
    s3_bucket = 'etl'
    s3_prefix_list = ['poke_api/items_attribute', 'poke_api/items']

    s3_client = S3Hook(aws_conn_id='aws_s3')

    for s3_prefix in s3_prefix_list:
        s3_files = s3_client.list_keys(bucket_name=s3_bucket, prefix=s3_prefix)

        for s3_file in s3_files:
            file_name = os.path.basename(s3_file)
            print(f"Downloaded file: {file_name}")
