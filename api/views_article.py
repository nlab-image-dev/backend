from datetime import datetime
import json
import datetime
from requests.api import delete

# from django.http import HttpResponse
# from django.views import View
from rest_framework import status, views, permissions
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import ArticleModel, TagModel


def get_articles():
    articles = ArticleModel.objects.all()
    articles_ls = []
    for art in articles:
        article = {
            'id': art.id,
            'title': art.title,
            'tag_id': art.tag.id if art.tag != None else 0,
            'text': art.text,
            'user_id': art.user.id,
            'posted_time': art.posted_time.timestamp(),
        }
        articles_ls.append(article)
    return articles_ls


def add_article(data):
    user = User.objects.get(id=data['user_id'])
    tag = TagModel.objects.get(id=data['tag_id'])

    article = ArticleModel(
        title = data['title'],
        tag = tag,
        text = data['text'],
        user = user,
        posted_time = datetime.datetime.now(),
    )

    article.save()

def delete_article(article_id):
    pass    

class ArticleView(views.APIView):
    # token認証
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        try:
            article_ls = get_articles()
            message = "success"
            status = 200
        except Exception as e:
            print(e)
            message = str(e)
            status = 500

        # JSON形式に整形
        send_data = {
            "message": message,
            "articles": article_ls if status==200 else [],
        }
        
        return Response(json.dumps(send_data), status=status)


    def post(self, request, *args, **kwargs):
        # postされたデータをJSONに変換
        recieve_data = json.loads(request.body)
        print(recieve_data)

        # postされたデータをデータベースへ登録する
        try:
            add_article(recieve_data)
            message = "success"
            status = 200
        except Exception as e:
            print(e)
            message = str(e)
            status = 500

        send_data = {
            "message": message,
        }
        return Response(json.dumps(send_data), status=status)


    def delete(self, request, *args, **kwargs):
        pass
