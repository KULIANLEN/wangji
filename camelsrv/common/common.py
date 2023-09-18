from django.http import HttpResponse
import json
from django.core.exceptions import *
import re

def format_response(code, msg, dat = {}):
    return HttpResponse(json.dumps({
            "code" : code,
            "msg" : msg,
            "dat" : dat
        }))

def raw_response(code, msg, dat = {}):
    return {
            "code" : code,
            "msg" : msg,
            "dat" : dat
        }

def format_raw(raw):
    return HttpResponse(json.dumps(raw))

def try_wrap(f):
    try:
        return f()
    except Exception as e:
        return format_response(-1, f"Server error : {str(e)}")

def get_base(id, query_methods, objects, model_name):
    ret = {}
    try:
        obj = objects.get(id = id)
    except ObjectDoesNotExist as e:
        return raw_response(-1, f"{model_name.capitalize()} {id} doesn't exist.")
    for k, v in query_methods.items():
        ret[k] = v(obj)
    return raw_response(1, "ok", ret)

def get_member_base(id, member_name, query_methods, objects, model_name):
    try:
        obj = objects.get(id = id)
    except ObjectDoesNotExist as e:
        return raw_response(-1, f"{model_name.capitalize()} {id} doesn't exist.")
    query_method = query_methods[member_name]
    if query_method == None:
        return raw_response(-1, f"{member_name.capitalize()} is not a member of user data.")
    return raw_response(1, "ok", query_method(obj))

def get_members_base(id, query_members, query_methods, objects, model_name):
    ret = {}
    try:
        obj = objects.get(id = id)
    except ObjectDoesNotExist as e:
        return raw_response(-1, f"{model_name.capitalize()} {id} doesn't exist.")
    for e in query_members:
        query_method = query_methods[e]
        if query_method == None:
            return raw_response(-1, f"{e} is not a member of {model_name} data.")
        ret[e] = query_method(obj)
    return raw_response(1, "ok", ret)
def query_base(req, id, query_methods, objects, model_name):
    query_members = req.GET.get('query')
    if query_members == None:
        return try_wrap(lambda: format_raw(get_base(id, query_methods, objects, model_name)))
    query_members = re.split(r"\|", query_members)
    return try_wrap(lambda: format_raw(get_members_base(id, query_members, query_methods, objects, model_name)))
def query_member_base(id, member_name, query_methods, objects, model_name):
    return try_wrap(lambda: format_raw(get_member_base(id, member_name, query_methods, objects, model_name)))