import mlflow
import pandas as pd


if __name__ == '__main__':
    # runs:/{Run ID}/titanic_model 이므로 {Run ID} 부분을 실행 대상 ID로 변경한다.
    logged_model = 'runs:/254c3097ed054cd89542bc079c9081fb/titanic_model'

    loaded_model = mlflow.pyfunc.load_model(logged_model)
    test_x = pd.DataFrame({"Pclass": [2, 1], "Sex": [0, 1], "Fare": [3.3211, 3.3211], "SibSp": [3, 3], "Parch":[3, 3]})
    print(loaded_model.predict(test_x))

