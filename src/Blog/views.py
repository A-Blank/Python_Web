from django.http import response
from django.http.response import HttpResponse
from Blog.models import Blog_Post
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from html.parser import HTMLParser



# Create your views here.

def Index(request):
    post_list = Blog_Post.objects.all()
#     for post in post_list:
#         html_parser = HTMLParser()
#         post.body = html_parser.unescape(post.body) 
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render_to_response('index.html',{'posts':posts})

def Post(request,post_id):
    post=Blog_Post.objects.get(pk=post_id)
    return render_to_response('post.html', {'post':post})
