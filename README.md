# Job Market Dataflow

## 專案簡介 (Project Overview)

本專案是一個使用 [Apache Airflow](https://airflow.apache.org/) 驅動的資料流程 (Dataflow) 系統，專門用於排程與執行分散式的網路爬蟲，以抓取各大求職網站的職缺資料。

主要的每日任務 (`all_producers_daily`) 會依序執行針對不同求職平台（例如：104、1111、CakeResume、Yourator）的爬蟲程式。

## 架構 (Architecture)

本系統採用以 Airflow 為核心的排程架構，並將每個爬蟲任務都封裝在獨立的 Docker 容器中執行，以達到環境隔離與高擴展性。

1.  **排程核心 (Scheduler)**: Airflow 作為系統的中央排程器，負責根據 `dags` 中定義的流程，每日定時觸發爬蟲任務。
2.  **任務執行 (Task Execution)**:
    *   每個爬蟲任務都是一個 Airflow 的 `DockerOperator` 實例。
    *   當任務啟動時，Airflow 會拉取指定的 Docker Image，並在容器中執行對應的爬蟲指令 (e.g., `python -m crawlers.104.producer`)。
    *   這種方式確保了每個爬蟲的執行環境與依賴套件都被獨立管理，不會互相衝突。
3.  **分散式任務佇列 (Distributed Task Queue)**:
    *   系統使用 Celery 作為任務執行器，並將爬蟲任務發送到指定的佇列 (`crawler-queue`)。
    *   這意味著可以部署多個 Airflow Worker 來監聽此佇列，並平行處理爬蟲任務，實現分散式抓取。

## 專案結構 (Project Structure)

```
.
├── Dockerfile
├── Pipfile
├── setup.py
└── src
    └── dataflow
        ├── dags/             # Airflow DAG 定義檔
        │   └── all_producers_daily.py
        └── etl/              # ETL 任務 (DockerOperator) 的定義
            ├── producer_104.py
            ├── producer_1111.py
            └── ...
```

*   `src/dataflow/dags/`: 存放 Airflow 的 DAG (有向無環圖) 定義檔，用來描述工作流程。
*   `src/dataflow/etl/`: 存放每個獨立 ETL 任務的設定檔，主要用於建立 `DockerOperator`。
*   `Pipfile` / `Pipfile.lock`: 定義本專案 (Airflow 環境) 的 Python 依賴套件。
*   `Dockerfile`: 用於建構執行 Airflow 服務 (Scheduler, Webserver, Worker) 的 Docker Image。

## 環境設定 (Setup) 和部署 (Deployment)

關於如何部署 Airflow 服務的詳細流程，請參考 `../docs/environment-and-deployment.md` 文件。