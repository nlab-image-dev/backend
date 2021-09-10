from datetime import datetime
import json

from django.db.models import Q
from rest_framework import status, views, permissions
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import ArticleModel, TagModel, ArticleTagsModel


def get_articles(data):
    '''
    articleを取得
    引数で取得内容を選択
    '''
    article_id = int(data['article_id']) if ('article_id' in data.keys()) else 0
    order_by = data['order_by'] if ('order_by' in data.keys()) else "id"
    reversed = int(data['reversed']) if ('reversed' in data.keys()) else 1
    start_num = int(data['start_num']) if ('start_num' in data.keys()) else 0
    end_num = int(data['end_num']) if ('end_num' in data.keys()) else -1
    username = data['username'] if ('username' in data.keys()) else None
    tag_id = int(data['tag_id']) if ('tag_id' in data.keys()) else 0
    keyword = data['keyword'] if ('keyword' in data.keys()) else None

    if article_id == 0:
        articles = ArticleModel.objects.all()
        if username is not None:
            # user_idで絞り込み
            articles = articles.filter(user__username__icontains=username)
        if tag_id != 0:
            # tag_idで絞り込み
            tag = TagModel.objects.get(id=tag_id)
            ids = [artag.article.id for artag in ArticleTagsModel.objects.filter(tag=tag)]
            articles = articles.filter(id__in=ids)
        if keyword is not None:
            #keywordでタイトル本文絞り込み
            articles = articles.filter(Q(title__icontains=keyword) | Q(text__icontains=keyword))

        # order byで並び変える
        if end_num == -1:
            articles = articles.order_by(order_by)
        else:
            articles = articles.order_by(order_by)[start_num:end_num]
        
    else:
        articles = ArticleModel.objects.filter(id=article_id)

    # Articleリスト作成
    articles_ls = []
    for art in articles:
        article = {
            'id': art.id,
            'title': art.title,
            'tags': [{"tag_id": article_tag.tag.id, "tag_name": article_tag.tag.tag_name} for article_tag in ArticleTagsModel.objects.filter(article_id=art.id)],
            'text': art.text,
            'user': {"user_id": art.user.id, "username": art.user.username},
            'posted_time': art.posted_time.timestamp(),
        }
        articles_ls.append(article)

    if reversed:
        articles_ls.reverse()

    return articles_ls

def add_article(user_id, data):
    '''
    articleを追加
    '''
    user = User.objects.get(id=user_id)

    article = ArticleModel(
        title = data['title'],
        text = data['text'],
        user = user,
        posted_time = datetime.now(),
    )
    article.save()

    tags = [TagModel.objects.get(id=tag_id) for tag_id in data['tag_ids']]
    for tag in tags:
        ArticleTagsModel(
            article = article,
            tag = tag,
        ).save()


def update_article(user_id, data):
    '''
    既存のarticleを編集
    '''
    article = ArticleModel.objects.filter(id=data['article_id'])
    if len(article) == 0:
        raise ValueError(f"Not found Article ID {data['article_id']}")

    if article[0].user.id != user_id:
        # 投稿者以外が編集しようとしたらエラー
        raise ValueError("You have no permission to edit this article!")

    # 記事内容の更新
    article.update(
        title = data['title'],
        text = data['text'],
    )

    # tagのつじつま合わせ
    artags = ArticleTagsModel.objects.filter(article=article[0])
    for artag in artags:
        # 消されたタグ
        if not artag.tag.id in data['tag_ids']:
            artag.delete()
    artag_tag_ids = [artag.tag.id for artag in artags]
    for tag_id in data['tag_ids']:
        # 増えたタグ
        if not tag_id in artag_tag_ids:
            ArticleTagsModel(
                article = article[0],
                tag = TagModel.objects.get(id=tag_id),
            ).save()

def delete_article(user_id, data):
    '''
    既存のarticleを削除
    '''
    article = ArticleModel.objects.get(id=data["article_id"])
    if article.user.id != user_id:
        # 投稿者以外が削除しようとしたらエラー
        raise ValueError("You have no permission to edit this article!")
    article.delete()



class ArticleView(views.APIView):
    # token認証
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        try:
            recieve_data = json.loads(request.body)
            print(recieve_data)
        except Exception as e:
            recieve_data = request.GET
            print(recieve_data)

        try:
            article_ls = get_articles(recieve_data)
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
            add_article(user_id=request.user.id, data=recieve_data)
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
            update_article(user_id=request.user.id, data=recieve_data)
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
            delete_article(user_id=request.user.id, data=recieve_data)
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

