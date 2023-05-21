import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

default_args = {
    'owner':'Varshini',
    'depends_on_past':False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email':'varshinisathish2112@gmail.com',
    'email_on_failure':True,
    'email_on_retry':True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'Uber_Data',
    default_args=default_args,
    description='Extract Hackers News Full data',
    schedule_interval="0 0 * * *"
)
 # t1 - import data from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page to GCS bucket 
 # if file already present, it should overwrite
 # bucket name = uber_data_analysis_raw_01 
 # Streaming insert - must provide object name as well
 # curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2009-01.parquet | gsutil cp - gs://uber_data_analysis_raw_01/input


t1 = BashOperator(
    task_id='Copy_to_GCS',
    dag=dag,
    depends_on_past=False,
    bash_command='curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2009-01.parquet | gsutil cp - gs://uber_data_analysis_raw_01/input'
)

