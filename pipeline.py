from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
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

gcpProjectName = "training-167208"
gcpClusterName = "meetup-cluster"
gcpRegion = "global"
gcpZone = "europe-west1-d"
# gcpDataStorage = "gs://meetup-bucket"
gcpJar = "g3://datalabs.devops/godomall/gelatolab-jobs_2.12-0.1.jar"
# gcpInitActions = 'gs://datlinq/dev/jobs/install-sql-proxy.sh'

start = DummyOperator(task_id='run_this_first', dag=dag)
end = DummyOperator(task_id='run_this_end', dag=dag)


# etl_facebook = DataProcSparkOperator(
#     task_id='t1_godomall',
#     execution_timeout=timedelta(minutes=30),
#     cluster_name=gcpClusterName,
#     dataproc_spark_jars=[gcpJar],
#     main_class='t1.BackupGodomallDB',
#     arguments=["aaa", "bbb"],
#     dag=dag)

start >> end
