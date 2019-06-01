from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import admin
from news.models import Post, Tag

URL = 'http://127.0.0.1:8000/'

def home(request, tag_slug=None):

    post_list = Post.objects.filter(visible='1')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "posts": posts,
        "title": "Main page",
        "desc": "main description",
        "key": "keywords",
    }
    return render(request, "partial/home.html", context)


def single(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post,
        "url": URL,
    }
    print(admin.site.urls)
    return render(request, "partial/single.html", context)


def tags_list(request, tag=None):
    posts = []
    for post in Post.objects.all():
        for post_tag in post.tag.all():
            if tag == str(post_tag):
                posts.append(post)

    return render(request, "partial/tags_list.html", context={'posts': posts, 'url': URL})
