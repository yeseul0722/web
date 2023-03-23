from django.db import models

# Create your models here.
def music(request):
    singer = models.CharField(max_length=10)
    title = models.TextField()