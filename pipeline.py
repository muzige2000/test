from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.dataproc_operator import DataProcSparkOperator, DataprocClusterCreateOperator, \
    DataprocClusterDeleteOperator, DataProcPySparkOperator
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 12, 4),
    'email': ['carlos@gelato.im'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}

dag = DAG('pipeline', default_args=default_args, schedule_interval=None, catchup=False)

start = DummyOperator(task_id='run_this_first', dag=dag)
end = DummyOperator(task_id='run_this_end', dag=dag)

start >> end
