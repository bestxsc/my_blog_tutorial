# -*- coding: utf-8 -*
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
def home(request): #主页面
    """return HttpResponse("Hello World,Django")"""
    post_list = Article.objects.all() #获取全部的Article对象
    return render(request,'base.html',{'post_list':post_list})
'''def detail(request,my_args): #输出url中的字符串
    return HttpResponse("You're lokking at my_args %s." % my_args)
'''
"""
def detail(request,my_args): #返回指定id（在url中输入id）的文章，以列表的形式返回
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})
"""