# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from django.views import View
from rest_framework.views import APIView
from api import models
import common.slfj_logger
import logging

logger = common.slfj_logger.Sl4jLogger()
logger_common = logging.getLogger('log')
django_logger = logging.getLogger('django')


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    s = hashlib.md5(bytes(user))
    s.update(bytes(ctime))
    return s.hexdigest()


class AuthView(APIView):

    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            username = request._request.GET.get('username')
            pwd = request._request.GET.get('password')
            obj = models.UserInfo.objects.filter(username=username, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            else:
                token = md5(username)
                token_obj = models.UserToken.objects.filter(user=obj).first()
                if not token_obj:
                    models.UserToken.objects.create(user=obj, token=token)
                else:
                    token_obj.token = token
                    token_obj.save()
                ret['msg'] = '登录成功'
                ret['token'] = token
        except Exception as e:
            print(e)
            ret['code'] = 1002
            ret['msg'] = '处理异常'

        return JsonResponse(ret)


def func(request):
    print("adasdas")
    data = {"a": 'b'}
    return JsonResponse(data)


def add(request):
    print("add student")
    params = request.GET
    if 'sex' in params:
        print("asd")
    if 'gender' in params:
        print("asdd")
    name = request.GET['name']
    age = request.GET['age']
    gender = request.GET['gender']
    stu = models.Student.objects.create(name=name, age=age, gender=gender)
    print("create student %s success", stu)
    stu_obj = {
        'name': stu.name,
        'age': stu.age,
        'gender': stu.gender
    }
    return JsonResponse(stu_obj)


def convert(stu):
    stu_obj = {
        'name': stu.name,
        'age': stu.age,
        'gender': stu.gender
    }
    return stu_obj


def query(request):
    ret = {'code': 1000, 'data': None, 'message': 'success'}
    params = request.GET
    conditions = {
    }
    for key in params:
        print(key)
        conditions[key] = params[key]
    results = models.Student.objects.filter(**conditions)
    result_list = []
    for item in results:
        result_list.append(convert(item))
    ret['data'] = result_list
    return JsonResponse(ret)


def success_resp(data):
    return JsonResponse({'code': 1000, 'data': data, 'message': 'success'})


def error_resp(code, message):
    return JsonResponse({'code': code, 'message': message, 'data': None})


def get_params(request):
    conditions = {}
    for key in request.GET:
        conditions[key] = request.GET[key]
    return conditions


def update(request):
    params = get_params(request)
    if 'id' not in params:
        return error_resp(1002, '没有学生id')
    stu_id = params.pop('id')
    result = models.Student.objects.filter(id=stu_id).update(**params)
    return success_resp(result)


def delete(request):
    params = get_params(request)
    row_number = models.Student.objects.filter(**params).delete()
    return success_resp(row_number)


def rest(request, id):
    return success_resp(convert(models.Student.objects.filter(id=id).first()))


def show(request):
    relation_list = models.Boy.objects.filter(name=u"lyf") \
        .first().relation_set.all()
    girl_list = []
    models.Relation.objects.filter(boy__name='lyf')
    for item_relation in relation_list:
        girl_list.append(item_relation.girl.name)

    print(girl_list)
    return success_resp(girl_list)


class CustomView(View):

    def dispatch(self, request, *args, **kwargs):
        print("dispatch execute!")
        print(request)
        print(request.method)
        print(request.path)
        return super(CustomView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        print("do get method!")
        print(request)
        return success_resp({})

    def post(self, request):
        print("do post method!")
        return success_resp({})


def login(request):
    logger.info("adasdad")
    logger_common.debug("common debug")
    logger_common.info("common info")
    logger_common.error("common error")
    django_logger.debug("django debug")
    django_logger.info("django info")
    django_logger.error("django error")
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('http://www.baidu.com')
        else:
            ret = {
                'username': username,
                'password': password,
                'msg': '用户名或密码错误'
            }
            return render(request, 'login.html', ret)
