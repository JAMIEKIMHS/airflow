from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp
# 로컬에서는 위의 common.common_func 경로를 찾지 못한다는 에러가 뜰 것임.
# 파이썬 인터프리터 가상환경을 만들 때, 프로젝트의 최상위 홈 디렉토리, 즉 airflow 디렉토리를
# path로 잡게 된다. 그래서 원래대로라면 plugins도 앞에 붙여줘야 한다.
# 그러나 plugins.common.common_func로 git 올렸다가 wsl로 받고 컨테이너 키면 에러 발생한다.
# 왜냐하면 에어플로우는 plugins 폴더까지 path로 잡혀있는 상태이기 때문이다.
# 그래서 common으로 시작하고 대신에 로컬에서 에러 안 나게 하려고 .env파일을 하나 만든다.

with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023,9,1,tz="Asia/Seoul"),
    catchup = False
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id = "task_get_sftp",
        python_callable=get_sftp
    )