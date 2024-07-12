from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    's3_sensor_dag',
    default_args=default_args,
    schedule_interval='@daily',
    tags=['custom', 'supratim']
)

s3_key_sensor = S3KeySensor(
    task_id='s3_key_sensor_task',
    bucket_name='etl',
    bucket_key='tests/test_file_3.txt',
    aws_conn_id='aws_s3',
    poke_interval=30,
    timeout=600,
    dag=dag,
)

s3_key_sensor
