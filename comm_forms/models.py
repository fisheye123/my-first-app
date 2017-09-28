from django.db import models
from news.models import Post


class Comm_Form(models.Model):
    book = models.ForeignKey(Post, verbose_name='Book')
    name = models.CharField('Name', max_length=100)
    date = models.DateTimeField('Date', auto_now_add=True)