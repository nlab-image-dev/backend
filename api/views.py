import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Test(View):
    def get(self, request, *args, **kwargs):
        # JSON形式に整形
        send_data = {
            "test": "hoge"
        }
        
        return HttpResponse(json.dumps(send_data), status=200)

    def post(self, request, *args, **kwargs):
        # postされたデータをJSONに変換
        recieve_data = json.loads(request.body)
        print(recieve_data)

        return HttpResponse()
