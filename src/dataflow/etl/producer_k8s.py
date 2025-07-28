# 從 Airflow 匯入 DockerOperator，用來在 DAG 中執行 Docker 容器任務
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def create_producer_task() -> KubernetesPodOperator:
    return KubernetesPodOperator(
        task_id="producer_crawler_finmind_duplicate",
        name="producer-crawler",
        namespace="default",
        image="linsamtw/tibame_crawler:0.0.8.composer",
        image_pull_policy='Always',  # 👈 強制每次都拉
        cmds=["pipenv", "run", "python", "crawler/producer_crawler_finmind_duplicate.py"],
        is_delete_operator_pod=True,
        get_logs=True,
    )
