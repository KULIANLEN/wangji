from django.shortcuts import render
from django.http import HttpResponse
import json
from . import models
# Create your views here.

def hello(request):
    try:
        a = int(request.GET.get('num1'))
        b = int(request.GET.get('num2'))
        ans = {'code':200,'res':a+b}
    except Exception as e:
        ans = {'code':-1,'res':'数据不合法'}
    return HttpResponse(json.dumps(ans))

def savedata(request):
    try:
        a = int(request.GET.get('num1'))
        b = int(request.GET.get('num2'))
        nums = models.num()
        nums.dat = a
        nums.name = b
        nums.save()
        for each in models.num.objects.all():
            print(each.name)
        res = {'code':200}
    except Exception as e:
        res = {'code':200}
    return HttpResponse(json.dumps(res))


