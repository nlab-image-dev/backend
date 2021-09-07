import requests
import datetime
import json

URL = "http://localhost:8000/api/"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IlRhcm8iLCJleHAiOjE2MzA5ODM3MjQsImVtYWlsIjoiIn0.CFiicXQkrvOqHS3_QX5e8TRj_cVdnAt6MHX2Efw0vfc"

def article_post(token):
    url = URL + "article/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "title": "aaa",
        "tag_id": 0,
        "text": "hoge",
        "user_id": 2,
    }

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.json())

def article_get():
    url = URL + "article/"
    response = requests.get(url)
    print(response.json())


def signup():
    url = URL + "signup/"
    headers = {
        "Content-Type" : "application/json"
    }
    data = {
        "username": "Taro",
        "password": "taro",
    }

    response = requests.post(url, json.dumps(data), headers=headers)

def login():
    url = URL + "login/"
    headers = {'Content-Type': 'application/json'}
    data = {'username': 'Taro', 'password': 'taro'}
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    # print(response, response.text)
    print(response.json())

    myinfo(response.json()['token'])

def myinfo(token):
    url = URL + "myinfo/"
    # GET
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    response = requests.get(url=url, headers=headers)
    print(response.json())



if __name__ == "__main__":
    article_post(TOKEN)
    # article_get()
    # signup()
    # login()
    # myinfo(TOKEN)
