# 從 Airflow 匯入 DockerOperator，用來在 DAG 中執行 Docker 容器任務
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from dataflow.constant import K8S_IMAGE

# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def create_producer_cake_task() -> KubernetesPodOperator:
    return KubernetesPodOperator(
        task_id="producer_cake_crawler",
        name="producer-cake-crawler",
        namespace="default",
        image=K8S_IMAGE,
        image_pull_policy='Always',  # 👈 強制每次都拉
        cmds=["pipenv", "run", "python", "-m", "crawlers.cake.producer"],
        is_delete_operator_pod=True,
        get_logs=True,
    )
