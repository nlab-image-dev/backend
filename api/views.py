from datetime import datetime
import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.contrib.auth.models import User
from .models import ArticleModel


def get_articles():
    articles = ArticleModel.objects.all()
    articles_ls = []
    for art in articles:
        article = {
            'id': art.id,
            'title': art.title,
            'tag_id': art.tag_id,
            'text': art.text,
            'posted_time': art.posted_time.timestamp(),
        }
        articles_ls.append(article)
    return articles_ls

def add_article(data):
    user = User.objects.get(id=data['user_id'])

    article = ArticleModel(
        title = data['title'],
        text = data['text'],
        user_id = user,
        posted_time = datetime.datetime.fromtimestamp(data['posted_time']),
    )
    article.save()


class Test(View):
    def get(self, request, *args, **kwargs):
        print(get_articles())
        # JSON形式に整形
        send_data = {
            "test": "hoge"
        }
        
        return HttpResponse(json.dumps(send_data), status=200)

    def post(self, request, *args, **kwargs):
        # postされたデータをJSONに変換
        recieve_data = json.loads(request.body)
        print(recieve_data)

        # postされたデータをデータベースへ登録する
        add_article(recieve_data)

        return HttpResponse()
