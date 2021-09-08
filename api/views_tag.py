import json

from rest_framework import status, views, permissions
from rest_framework.response import Response

from .models import TagModel

def get_tags(data):
    '''
    タグ一覧を取得
    '''
    tag_id = data["tag_id"] if('tag_id' in data.keys()) else 0
    keyword = data["keyword"] if('keyword' in data.keys()) else None

    if tag_id == 0:
        tags = TagModel.objects.all()
        if keyword is not None:
            tags = tags.filter(tag_name__icontains=keyword)
    else:
        tags = TagModel.objects.filter(id=tag_id)

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
    if len(TagModel.objects.filter(tag_name=data['tag_name'])) > 0:
        raise ValueError(f"'{data['tag_name']}' already exists!")
    tag = TagModel(
        tag_name = data['tag_name'],
    )

    tag.save()

class TagView(views.APIView):
    # token認証
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        try:
            recieve_data = json.loads(request.body)
            print(recieve_data)
        except Exception as e:
            recieve_data = {}

        try:
            tags_ls = get_tags(recieve_data)
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