from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from .views import Test
from .views_user import *
from .views_article import ArticleView
from .views_tag import TagView
from .views_comment import CommentView

urlpatterns = [
    path('test/', Test.as_view(), name="test"),

    path('login/', obtain_jwt_token, name="login"),
    path('signup/', AuthRegister.as_view(), name="signup"),
    path('myinfo/', AuthInfoGetView.as_view(), name="myinfo"),

    path('article/', ArticleView.as_view(), name="article"),

    path('tag/', TagView.as_view(), name="tag"),

    path('comment/<int:article_id>/', CommentView.as_view(), name="comment")
]