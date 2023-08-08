# MLFlow 101 (Korean) with Titanic data

[MLflow](https://mlflow.org/) 실험, 실행, 모델 단위 등을 [Kaggle에 공개된 Titanic 데이터셋](https://www.kaggle.com/competitions/titanic/)을 기반으로 트레이닝, 인퍼런스를 실행하며 배워보는 튜토리얼입니다.

본 튜토리얼은 [MLflow_tutorial](https://github.com/vhrehfdl/mlflow_tutorial) 자료를 기반으로 현재 (2023년 8월 기준) MLflow 최신 버전인 2.5를 기준으로 재작성되었습니다.

## 가상 환경 (Virtual Environment)

`venv`라는 가상 환경을 만들고 `requirements.txt`에 명시된 패키지를 pip로 설치하는 명령어입니다.

만약 `pyenv`, `conda` 등을 사용하고자 한다면 아래를 참고하여 적절히 변경해 사용하세요.

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Tracking

실험 결과 자동 저장 및 관리 UI 화면을 살펴봅니다.

```
# 현재 경로: ML
$ cd ML 
# 해당 파일 내 run id를 변경하고 실행합니다.
$ python mlflow_tracking.py
YYYY/MM/DD HH:MM:SS INFO mlflow.tracking.fluent: Experiment with name 'titanic' does not exist. Creating a new experiment.

$ mlflow ui
```

## Inference

저장된 모델에 실행했던 대상을 지정하여 추론을 해봅니다.

```
# 현재 경로: ML
$ cd ../ML

$ python mlflow_inference.py
```

## 모델 서빙

모델 API 서버 띄우기
```
# 터미널1 - 아래 run id를 변경하여 실행합니다.
$ mlflow models serve -m runs:/254c3097ed054cd89542bc079c9081fb/titanic_model --no-conda --port 5001

# 터미널2 - API 실행 테스트
$ curl -d '{"dataframe_split": {"columns": ["Pclass", "Sex", "Fare", "SibSp", "Parch"],"data": [[1, 2, 3, 2 ,2], [1, 2, 4, 5, 6]]}}' \
-H 'Content-Type: application/json' -X POST 127.0.0.1:5001/invocations
```

## Registry - Tracking Server

MLflow Tracking Server 같은 경우에는 터미널을 2개 띄운 후 실행합니다.
```
[터미널 A]
# 현재 경로가 ML이라고 가정하여 아래 명령어를 참고합니다.
$ cd ..
$ mkdir tracking_server
$ cd tracking_server
# 아래 경로를 적절히 수정하여 실행 필요
$ mlflow server --backend-store-uri file:/home/user/MLflow-101/tracking_server --default-artifact-root /home/user/MLflow-101/tracking_server --port 5000
```

mlflow_tracking.py에서 "mlflow.set_tracking_uri("http://IP주소:포트")" 관련 4줄 코드 주석을 해제하고, 그 아래 2줄을 주석 처리 후 실행
```
[터미널 B]
# 현재 경로가 ML이라고 가정
$ cd ../ML
$ python mlflow_tracking.py
```

웹 UI를 통해 결과를 확인해봅니다 (http://localhost:5000).

## 그 외 참고

- MLflow-101.pdf: 발표 자료
- request_test.py: 배포된 API를 Python 코드로 호출