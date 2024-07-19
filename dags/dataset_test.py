from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.models.variable import Variable
from airflow.providers.amazon.aws.operators.s3 import S3FileTransformOperator


SOURCE_KEY = Variable.get("s3_source_key", "s3://etl/test_file_1.txt")
DEST_KEY = Variable.get("s3_dest_key", "s3://etl/tests/test_file_1.txt")

DEFAULT_ARGS = {
    'schedule_interval': '@once',
    'catchup': False,
}

with DAG(
    dag_id='localstack_concept_example',
    default_args=DEFAULT_ARGS,
    tags=['custom', 'supratim']
) as dag:

    starting_process = BashOperator(
        task_id='starting_process',
        bash_command="echo starting process"
    )

    transforming_s3_file = S3FileTransformOperator(
        source_aws_conn_id='aws_s3',
        task_id='transforming_s3_file',
        source_s3_key=SOURCE_KEY,
        dest_aws_conn_id='aws_s3',
        dest_s3_key=DEST_KEY,
        transform_script="/bin/cp",
        replace=False
    )

    end_process = BashOperator(
        task_id='end_process',
        bash_command="echo SUCCESS!"
    )


    starting_process >> transforming_s3_file >> end_process
    