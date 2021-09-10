import requests
import datetime
import json

URL = "http://localhost:8000/api/"

# URL = "https://nlab-image-dev.herokuapp.com/api/"



def signup(username, password):
    url = URL + "signup/"
    headers = {
        "Content-Type" : "application/json"
    }
    data = {
        "username": username,
        "password": password,
    }

    response = requests.post(url, json.dumps(data), headers=headers)
    print(response, response.text)
    print(response.json())

def login(username, password):
    url = URL + "login/"
    headers = {'Content-Type': 'application/json'}
    data = {'username': username, 'password': password}
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response, response.text)
    # print(response.json())

    return response.json()['token']

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
        "title": "new research",
        "tag_ids": [1, 2],
        "text": "gan+cellular",
    }

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.json())

def article_get():
    url = URL + "article/"
    data = {
        # "article_id": 1,
        # "start_num": 0,
        # "end_num": 20,
        # "username": "admin",
        # "tag_id": 1,
        # "keyword": "hogehoge",
    }
    # response = requests.get(url, data=json.dumps(data))
    response = requests.get(url)
    print(response.json())
    # print(json.loads(response.json())["articles"][0]["user"]["username"])

def article_put(token):
    url = URL + "article/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "article_id": 10,
        "title": "gan",
        "tag_ids": [1,2],
        "text": "gan+aux",
    }

    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.json())

def article_delete(token):
    url = URL + "article/"
    headers = {'Content-Type': 'application/json', 'Authorization': f'JWT {token}'}
    data = {
        "article_id": 9
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
    }

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.json())


if __name__ == "__main__":
    # signup("admin", "admin")
    # TOKEN = login("admin", "admin")
    # myinfo(TOKEN)

    # article_post(TOKEN)
    article_get()
    # article_put(TOKEN)
    # article_delete(TOKEN)
    # article_get()

    # tag_post(TOKEN)
    # tag_get()

    # comment_post(TOKEN)
    # comment_get()
