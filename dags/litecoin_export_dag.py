from __future__ import print_function

from datetime import datetime

from airflow.models import Variable

from bitcoinetl.build_export_dag import build_export_dag

start_date = Variable.get('litecoin_export_start_date', '2011-10-07')
# When searching for DAGs, Airflow will only consider files where the string “airflow” and “DAG” both appear in the
# contents of the .py file.
DAG = build_export_dag(
    dag_id='litecoin_export_dag',
    provider_uri=Variable.get('litecoin_provider_uri'),
    output_bucket=Variable.get('litecoin_output_bucket'),
    start_date=datetime.strptime(start_date, '%Y-%m-%d'),
    chain='litecoin',
    notification_emails=Variable.get('notification_emails', ''),
    schedule_interval='0 5 * * *',
    export_max_workers=4,
    export_batch_size=4
)
