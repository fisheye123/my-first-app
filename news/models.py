from django.db import models
from django.utils import timezone

GET_SHORT_TEXT = 300


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > GET_SHORT_TEXT:
            return self.text[:GET_SHORT_TEXT]
        else:
            return self.text


class Comments(models.Model):
    date = models.DateTimeField(default=timezone.now)

    # date = models.DateTimeField('Date', auto_now_add=True)
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    comments_text = models.TextField(verbose_name='Комментарии')
    comments_article = models.ForeignKey(Post)
