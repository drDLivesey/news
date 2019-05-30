from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from news.models import Post


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
    }
    return render(request, "partial/single.html", context)

