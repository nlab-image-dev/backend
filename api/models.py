from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TagModel(models.Model):
    tag_name = models.CharField(max_length=20)
    
class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(TagModel, on_delete=models.PROTECT, null=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_time = models.DateTimeField()
    file = models.FileField(upload_to="media/%Y%m%d/", null=True)

class CommentModel(models.Model):
    text = models.TextField()
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_time = models.DateTimeField()
    

