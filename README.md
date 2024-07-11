## Custom Stuff

### Connections

#### localstack connection
---
```
access_key_id: localstack
secret_access_key: localstack
type: Amazon Web Services
extra_args:
{
    "region_name": "us-west-2", 
    "aws_access_key_id": "test", 
    "aws_secret_access_key": "test", 
    "endpoint_url": "http://localstack:4566"
}
```


#### PokeAPI connection
```
type: HTTP
host: "https://pokeapi.co/api/v2"
```

### Easy way to setup
After all the containers are up and running, check the airflow webserver container name, in my case it's `airflow-airflow-webserver-1`, copy the connection config to this container at `/opt/airflow` and use the `airflow-webserver` service to import it
```
# copy the connections config to airflow webserver container
docker cp config/connections.json airflow-airflow-webserver-1:/opt/airflow

# import the connection in airflow webserver service
docker-compose exec airflow-webserver airflow connections import connections.json
```


### Commands

#### dataset_test
```
AWS_ACCESS_KEY_ID=localstack AWS_SECRET_ACCESS_KEY=localstack aws --endpoint-url=http://localhost:4566 --region=$AWS_S3_REGION s3 mb s3://etl
AWS_ACCESS_KEY_ID=localstack AWS_SECRET_ACCESS_KEY=localstack aws --endpoint-url=http://localhost:4566 --region=$AWS_S3_REGION s3 cp data/test_file_1.txt s3://etl/test_file_1.txt
```


#### dag_factory
```
AWS_ACCESS_KEY_ID=localstack AWS_SECRET_ACCESS_KEY=localstack aws --endpoint-url=http://localhost:4566 --region=$AWS_S3_REGION s3 mb s3://etl
```