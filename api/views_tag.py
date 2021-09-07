import json

from rest_framework import status, views, permissions
from rest_framework.response import Response

from .models import TagModel

def get_tags():
    '''
    タグ一覧を取得
    '''
    tags = TagModel.objects.all()

    tags_ls = []
    for tag in tags:
        tag_dict = {
            "id": tag.id,
            "name": tag.tag_name,
        }
        tags_ls.append(tag_dict)

    return tags_ls

def add_tag(data):
    '''
    タグを追加
    '''
    tag = TagModel(
        tag_name = data['tag_name'],
    )

    tag.save()

class TagView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            tags_ls = get_tags()
            status = 200
            message = "success"
        except Exception as e:
            print(e)
            status = 500
            message = str(e)

        send_data = {
            "message": message,
            "tags": tags_ls,
        }
        return Response(json.dumps(send_data), status=status)

    def post(self, request, *args, **kwargs):
        recieve_data = json.loads(request.body)
        print(recieve_data)

        try:
            add_tag(recieve_data)
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