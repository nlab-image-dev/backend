import json

from rest_framework import status, views, permissions
from rest_framework.response import Response



class CommentView(views.APIView):
    def get(self, request, *args, **kwargs):

        status = 200
        send_data = {
            "message": "yet",
        }
        return Response(json.dumps(send_data), status=status)

    def post(self, request, *args, **kwargs):

        status = 200
        send_data = {
            "message": "yet",
        }
        return Response(json.dumps(send_data), status=status)