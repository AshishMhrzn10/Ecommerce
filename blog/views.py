from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    myPost = Blogpost.objects.all()
    return render(request, 'blog/index.html',{'myPost':myPost})   


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html',{'post':post})
