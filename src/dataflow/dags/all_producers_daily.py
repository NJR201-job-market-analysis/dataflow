import airflow
from dataflow.constant import (
    DEFAULT_ARGS,
    MAX_ACTIVE_RUNS,
)
from dataflow.etl.producer_104 import create_producer_104_task
from dataflow.etl.producer_1111 import create_producer_1111_task
from dataflow.etl.producer_cake import create_producer_cake_task
from dataflow.etl.producer_yourator import create_producer_yourator_task

with airflow.DAG(
    dag_id="all_producers_daily",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    max_active_runs=MAX_ACTIVE_RUNS,
    catchup=False,
    doc_md="Runs all crawler producers sequentially.",
    tags=["crawler", "producer", "all"],
) as dag:
    task_104 = create_producer_104_task()
    task_1111 = create_producer_1111_task()
    task_cake = create_producer_cake_task()
    task_yourator = create_producer_yourator_task()

    # Set trigger rules for all downstream tasks
    task_1111.trigger_rule = "all_done"
    task_cake.trigger_rule = "all_done"
    task_yourator.trigger_rule = "all_done"

    task_104 >> task_1111 >> task_cake >> task_yourator