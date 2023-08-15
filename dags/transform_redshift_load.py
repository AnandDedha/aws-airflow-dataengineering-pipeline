from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.sensors.external_task_sensor import ExternalTaskMarker, ExternalTaskSensor
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('transform_redshift_dag', default_args=default_args, schedule_interval="@once",catchup=False)


# Define the Glue Job
transform_task = GlueJobOperator(
    task_id='transform_task',
    job_name='glue_transform_task',
    script_location='s3://aws-glue-assets-262136919150-us-east-1/scripts/transform.py',
    s3_bucket='s3://aws-glue-assets-262136919150-us-east-1',  # S3 bucket where logs and local etl script will be uploaded
    aws_conn_id='AWS_CONN',  # You'll need to set up an AWS connection in Airflow
    region_name="us-east-1",
    iam_role_name='datapipeline-demo-RedshiftIamRole-1KQUQK6ZER2WH',
    create_job_kwargs ={"GlueVersion": "4.0", "NumberOfWorkers": 4, "WorkerType": "G.1X", "Connections":{"Connections":["redshift-demo-connection"]},},
    dag=dag,
)

wait_openweather_api = ExternalTaskSensor(
    task_id='wait_openweather_api',
    external_dag_id = 'openweather_api_dag',
    external_task_id = None,
    timeout=2000,
    dag=dag,
    mode ='reschedule',
    allowed_states=["success"]
)
    
# Set task dependencies
wait_openweather_api >> transform_task
