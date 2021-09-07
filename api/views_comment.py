import json
from datetime import datetime

from rest_framework import status, views, permissions
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import CommentModel, ArticleModel

def get_comments(article_id):
    comments = CommentModel.objects.filter(article_id=article_id).order_by("posted_time")

    comments_ls = []
    for com in comments:
        comment_dict = {
            "id": com.id,
            "text": com.text,
            "user": {"user_id": com.user.id, "username": com.user.username},
            "posted_time": com.posted_time.timestamp()
        }
        comments_ls.append(comment_dict)
    
    return comments_ls

def add_comment(article_id, data):
    article = ArticleModel.objects.get(id=article_id)
    user = User.objects.get(id=data["user_id"])

    comment = CommentModel(
        text = data["text"],
        article = article,
        user = user,
        posted_time = datetime.now(),
    )

    comment.save()



class CommentView(views.APIView):
    # token認証
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, article_id, *args, **kwargs):
        try:
            comments_ls = get_comments(article_id)
            status = 200
            message = "success"
        except Exception as e:
            print(e)
            status = 500
            message = str(e)

        send_data = {
            "message": message,
            "comments": comments_ls,
        }
        return Response(json.dumps(send_data), status=status)

    def post(self, request, article_id, *args, **kwargs):
        recieve_data = json.loads(request.body)
        print(recieve_data)

        try:
            add_comment(article_id, recieve_data)
            status = 200
            message = "success"
        except Exception as e:
            print(e)
            status = 500
            message = str(e)    

        send_data = {
            "message": message,
        }
        return Response(json.dumps(send_data), status=status)