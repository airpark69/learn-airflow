import requests
from requests.auth import HTTPBasicAuth

# Airflow 웹서버 URL
base_url = 'http://34.64.84.88:8080/api/v1'

# Airflow DAGs 리스트 API endpoint
endpoint = '/dags'

# 요청 URL 합치기
url = base_url + endpoint

# 사용자 이름과 비밀번호 설정
username = 'admin2'
password = 'admin2'

# GET 요청 보내기
response = requests.get(url, auth=HTTPBasicAuth(username, password))

print(response.status_code)  # 응답 상태 코드 출력
print(response.text)  # 응답 내용 출력

# 응답에서 JSON 가져오기
dags = response.json()

# 출력
print(dags)
