from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def process_data():
    # Implement your data processing logic here
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A simple data pipeline',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

process = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> process >> end
