from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class TagModel(models.Model):
    tag_name = models.CharField(max_length=20)
    
class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_time = models.DateTimeField()
    file = models.FileField(upload_to="media/%Y%m%d/", null=True)

class ArticleTagsModel(models.Model):
    article = ForeignKey(ArticleModel, on_delete=models.CASCADE)
    tag = ForeignKey(TagModel, on_delete=models.CASCADE)

class CommentModel(models.Model):
    text = models.TextField()
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_time = models.DateTimeField()


    

