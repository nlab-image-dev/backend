import requests
import datetime
import json

def article_post():
    url = "http://localhost:8000/api/test/"
    data = {
        "title": "aaa",
        "tag_id": 1,
        "text": "aaaaaa",
        "user_id": 1,
        "posted_time": datetime.datetime.now().timestamp(),
    }

    requests.post(url, json.dumps(data))


def signup():
    url = "http://localhost:8000/api/signup/"
    headers = {
        "Content-Type" : "application/json"
    }
    data = {
        "username": "Taro",
        "password": "taro",
    }

    response = requests.post(url, json.dumps(data), headers=headers)

def login():
    url = "http://localhost:8000/api/login/"
    headers = {'Content-Type': 'application/json'}
    data = {'username': 'Taro', 'password': 'taro'}
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    # print(response, response.text)
    print(response.json())

    myinfo(response.json()['token'])

def myinfo(token):
    url = "http://localhost:8000/api/myinfo/"
    # GET
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    response = requests.get(url=url, headers=headers)
    print(response.json())



if __name__ == "__main__":
    # article_post()
    # signup()
    login()