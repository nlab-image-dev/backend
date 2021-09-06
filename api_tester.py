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

    requests.post(url, json.dumps(data), headers=headers)

def login():
    pass

if __name__ == "__main__":
    article_post()
    # signup()