from airflow import settings
from airflow.models import DagBag

dag_bag = DagBag(settings.DAGS_FOLDER)
print(dag_bag.dags)
