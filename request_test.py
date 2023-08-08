import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'dataframe_split': {
        'columns': ['Pclass', 'Sex', 'Fare', 'SibSp', 'Parch'],
        'data': [
            [1, 2, 3, 2, 2],
            [1, 2, 4, 5, 6],
        ],
    }
}

## For backword compatibility: MLflow 1.x
# json_data = {
#     'columns': ['Pclass', 'Sex', 'Fare', 'SibSp', 'Parch'],
#     'data': [
#         [1, 2, 3, 2, 2],
#         [1, 2, 4, 5, 6],
#     ],
# }

response = requests.post('http://127.0.0.1:5001/invocations', headers=headers, json=json_data)

print(response.text)
