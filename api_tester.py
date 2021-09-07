import requests
import datetime
import json

URL = "http://localhost:8000/api/"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IlRhcm8iLCJleHAiOjE2MzA5ODM3MjQsImVtYWlsIjoiIn0.CFiicXQkrvOqHS3_QX5e8TRj_cVdnAt6MHX2Efw0vfc"

# URL = "https://nlab-image-dev.herokuapp.com/api/"
# TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IlRhcm8iLCJleHAiOjE2MzA5OTcyMjcsImVtYWlsIjoiIn0.6V7AO-pdiUY_FMK2jw3SlMGpuYwG3aXOmfIhmpsnetM"



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
    print(response, response.text)
    print(response.json())

def login():
    url = URL + "login/"
    headers = {'Content-Type': 'application/json'}
    data = {'username': 'Taro', 'password': 'taro'}
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response, response.text)
    print(response.json())

    # myinfo(response.json()['token'])

def myinfo(token):
    url = URL + "myinfo/"
    # GET
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    response = requests.get(url=url, headers=headers)
    print(response, response.text)
    print(response.json())




def article_post(token):
    url = URL + "article/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "title": "gan",
        "tag_ids": [1, 2],
        "text": "gan+aux",
        "user_id": 1,
    }

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.json())

def article_get():
    url = URL + "article/"
    data = {
        # "article_id": 1,
        "start_num": 0,
        "end_num": 10,
        # "user_id": 2,
        "tag_id": 1,
        # "keyword": "hogehoge",
    }
    response = requests.get(url, data=json.dumps(data))
    print(response.json())

def article_put(token):
    url = URL + "article/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "article_id": 11,
        "title": "aaa",
        "tag_ids": [1,2],
        "text": "hogehoge",
    }

    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.json())

def article_delete(token):
    url = URL + "article/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "article_id": 11
    }

    response = requests.delete(url=url, data=json.dumps(data), headers=headers)
    print(response.json())


def tag_get():
    url = URL + "tag/"
    data = {
        # "tag_id": 1,
        "keyword": "浸透",
    }

    response = requests.get(url, data=json.dumps(data))
    print(response.json())

def tag_post(token):
    url = URL + "tag/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "tag_name": "浸透学習"
    }

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.json())


def comment_get():
    url = URL + "comment/1/"

    response = requests.get(url)
    print(response.json())

def comment_post(token):
    url = URL + "comment/1/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "text": "abccba",
        "user_id": 2,
    }

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.json())


if __name__ == "__main__":
    # signup()
    # login()
    # myinfo(TOKEN)

    # article_post(TOKEN)
    # article_get()
    # article_put(TOKEN)
    # article_delete(TOKEN)
    article_get()

    # tag_post(TOKEN)
    # tag_get()

    # comment_post(TOKEN)
    # comment_get()
