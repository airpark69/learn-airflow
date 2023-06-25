import os
import requests
from requests.auth import HTTPBasicAuth

# Airflow 웹서버 URL
base_url = 'http://34.64.127.133:8080/api/v1'

# Airflow DAGs 리스트 API endpoint
endpoint = '/dags'

url = base_url + endpoint

# 사용자 이름과 비밀번호 설정
username = os.getenv('AIRFLOW_RESTAPI_USERNAME')
password = os.getenv('AIRFLOW_RESTAPI_PASSWORD')

# GET 요청 보내기
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# 응답에서 JSON 가져오기
dags = response.json()


if response.status_code == 200:
# dags 내부의 활성화된 dag인 경우 값이 True
    for dag in dags['dags']:
        if dag['is_paused'] == False:
            print(dag['dag_id'])

else:
    print("Error code : %s" % response.status_code)

