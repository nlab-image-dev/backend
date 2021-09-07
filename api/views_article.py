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


def get_articles(article_id=0, order_by="posted_time", start_num=0, end_num=10, user_id=0, tag_id=0):
    '''
    articleを取得
    引数で取得内容を選択
    '''
    if article_id == 0:
        articles = ArticleModel.objects.all()
        if user_id != 0:
            # user_idで絞り込み
            user = User.objects.get(id=user_id)
            articles = articles.filter(user=user)
        if tag_id != 0:
            # tag_idで絞り込み
            tag = TagModel.objects.get(id=tag_id)
            articles = articles.filter(tag=tag)
        # order byで並び変える
        articles = articles.order_by(order_by)[start_num:end_num]
    else:
        articles = ArticleModel.objects.filter(id=article_id)

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
    '''
    articleを追加
    '''
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

def update_article(data):
    '''
    既存のarticleを編集
    '''
    tag = TagModel.objects.get(id=data['tag_id'])

    ArticleModel.objects.filter(id=data['article_id']).update(
        title = data['title'],
        tag = tag,
        text = data['text'],
    )

def delete_article(article_id):
    '''
    既存のarticleを削除
    '''
    ArticleModel.objects.get(id=article_id).delete()



class ArticleView(views.APIView):
    # token認証
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        recieve_data = json.loads(request.body)
        print(recieve_data)

        article_id = recieve_data['article_id'] if ('article_id' in recieve_data.keys()) else 0
        order_by = recieve_data['order_by'] if ('order_by' in recieve_data.keys()) else "posted_time"
        start_num = recieve_data['start_num'] if ('start_num' in recieve_data.keys()) else 0
        end_num = recieve_data['end_num'] if ('end_num' in recieve_data.keys()) else 10
        user_id = recieve_data['user_id'] if ('user_id' in recieve_data.keys()) else 0
        tag_id = recieve_data['tag_id'] if ('tag_id' in recieve_data.keys()) else 0

        try:
            article_ls = get_articles(article_id=article_id, order_by=order_by, start_num=start_num, end_num=end_num, user_id=user_id, tag_id=tag_id)
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


    def put(self, request, *args, **kwargs):
        # postされたデータをJSONに変換
        recieve_data = json.loads(request.body)
        print(recieve_data)

        # postされたデータをデータベースへ登録する
        try:
            update_article(recieve_data)
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
        # postされたデータをJSONに変換
        recieve_data = json.loads(request.body)
        print(recieve_data)

        try:
            delete_article(recieve_data["article_id"])
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

