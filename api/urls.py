from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from .views import Test
from .views_user import *
from .views_article import ArticleView

urlpatterns = [
    path('test/', Test.as_view(), name="test"),

    path('login/', obtain_jwt_token, name="login"),
    path('signup/', AuthRegister.as_view(), name="signup"),
    path('myinfo/', AuthInfoGetView.as_view(), name="myinfo"),

    path('article/', ArticleView.as_view(), name="article"),
]