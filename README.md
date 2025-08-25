# dataflow

# 環境設定

#### 安裝 pipenv

    pip install pipenv==2022.4.8

#### set pipenv

    pipenv --python ~/.pyenv/versions/3.8.10/bin/python

#### 安裝 repo 套件

    pipenv sync

#### 建立環境變數

    ENV=DEV python genenv.py
    ENV=DOCKER python genenv.py
    ENV=PRODUCTION python genenv.py

#### 排版

    black -l 80 src/

# Docker

#### build docker image

    docker build -f Dockerfile -t account_name/jobmarket-dataflow:0.0.1 .
    docker build -f Dockerfile -t account_name/jobmarket-dataflow:0.0.1.arm64 .
    docker build -f gce.with.env.Dockerfile -t account_name/jobmarket-dataflow:0.0.6.gce .

#### push docker image

    docker push account_name/jobmarket-dataflow:0.0.1
    docker push account_name/jobmarket-dataflow:0.0.1.arm64
    docker push account_name/jobmarket-dataflow:0.0.6.gce

#### pull docker image

    docker pull account_name/jobmarket-dataflow:0.0.1
    docker pull account_name/jobmarket-dataflow:0.0.1.arm64
    docker pull account_name/jobmarket-dataflow:0.0.1.gce

## deploy-airflow:
	DOCKER_IMAGE_VERSION=0.0.1 docker stack deploy --with-registry-auth -c docker-compose-airflow.yml airflow
	DOCKER_IMAGE_VERSION=0.0.1.arm64 docker stack deploy --with-registry-auth -c docker-compose-airflow.yml airflow
	DOCKER_IMAGE_VERSION=0.0.1.gce docker stack deploy --with-registry-auth -c docker-compose-airflow.yml airflow

## 調整筆電 gcloud project
    gcloud config set project airflow-466005

## 上傳程式碼到 Composer
	gcloud composer \
	environments storage \
	dags import --environment airflow  \
	--location us-central1 \
	--source "src/dataflow" 

