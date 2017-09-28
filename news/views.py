from django.utils import timezone
from .models import Post, Comments
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, NewsFilterForm, CommentFrom
from comm_forms.forms import Comm_Form_Forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(comments_article=pk)
    form = Comm_Form_Forms(request.POST or None, initial={'post': post})
    form_comments = CommentFrom
    username = auth.get_user(request).username
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=True".format(reverse('post', kwargs={'pk': pk})))
    return render(request, 'news/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'form_comments': form_comments,
        'username': username,
        'sended': request.GET.get('sended', False)
    })


def addcomment(request, pk):
    if request.method == "POST" and ("pause" not in request.session):
        form = CommentFrom(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Post.objects.get(pk=pk)
            form.save()
            request.session.set_expiry(30)
            request.session["pause"] = True
    #return HttpResponseRedirect('/')
    return HttpResponseRedirect('/newsfeed/post/%s/' % pk)
    #return HttpResponseRedirect("{}?".format(reverse(kwargs={'pk': pk})))

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_edit.html', {'form': form})


def post_filter(request):
    posts = Post.objects.all()
    form = NewsFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["ordering"]:
            posts = posts.order_by(form.cleaned_data["ordering"])
    context = {"posts": posts, "form": form}
    return render(request, 'news/post_filter.html', context)
