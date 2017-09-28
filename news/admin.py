from django.contrib import admin
from .models import Post, Comments


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class AdminArticle(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]
    inlines = [ArticleInline]


admin.site.register(Post, AdminArticle)
