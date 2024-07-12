from airflow.models import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.datasets import Dataset


dag1_dataset = Dataset("s3://etl/tests/test_file_1.txt")
dag2_dataset = Dataset("s3://etl/tests/test_file_2.txt")


with DAG(
    dag_id='dataset_as_schedule',
    schedule=[dag1_dataset, dag2_dataset],
    start_date=datetime(2023, 7, 11),
    tags=["supratim", "custom"]
) as dag:

    starting_process = BashOperator(
        task_id='starting_process',
        bash_command="echo starting process"
    )

    middle_process = BashOperator(
        task_id='bash_task',
        bash_command='echo "I am scheduled"',
    )

    end_process = BashOperator(
        task_id='end_process',
        bash_command="echo SUCCESS!"
    )


    starting_process >> middle_process >> end_process
