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
        return format_response(-1, f"Server error: {str(e)}")
class Noref():
    pass

def try_deref(obj, members):
        if hasattr(obj, 'query_methods'):
            return get_member_recursive(obj, members)
        elif isinstance(obj, list):
            ret = list(filter(lambda e : e != Noref, map(lambda e : try_deref(e, members), obj)))
            return ret
        elif isinstance(obj, dict):
            ret = dict(filter(lambda t : t[1] != Noref, map(lambda t : (t[0], try_deref(t[1], members)), obj)))
        else:
            return obj

def get_member_recursive(obj, members):
    if hasattr(members, 'wild'):
        return dict(filter(lambda t: t[1] != Noref, map(lambda t: (t[0], try_deref(t[1](), members.wild)), obj.query_methods().items())))
    return dict(filter(lambda t: t[1] != Noref, 
                       map(lambda t: (t[0], try_deref(obj.query_methods()[t[0]]() if t[0] in obj.query_methods() else Noref, t[1])), members.items())))

def get_base(id, objects):
    ret = {}
    try:
        obj = objects.get(id = id)
    except ObjectDoesNotExist as e:
        return raw_response(-1, f"{id} doesn't exist.")
    for k, v in obj.query_methods().items():
        ret[k] = try_deref(v(), {})
    return raw_response(1, "ok", ret)

def parse_member_set(param, idx = 0):
    ret = {}
    while param[idx] != '}':
        idx += 1
        res = parse_members_param(param, idx)
        idx = res[1]
        ret.update(res[0])
    return (ret, idx + 1)
class wild():
    wild = True
    def __init__(self, val) -> None:
        self.wild = val
    
def parse_members_param(param, idx = 0):
    if param[idx] == '*':
        if len(param) > idx + 1 and param[idx + 1] == '.':
            sub = parse_members_param(param, idx + 2)
            return (wild(sub[0]), sub[1])
        return (wild({}), idx + 1)
    if param[idx] == '{':
        sub = parse_member_set(param, idx)
        return (sub[0], sub[1])
    res = re.search(r'^\w+', param[idx:])
    if len(param) > idx + res.end() and param[idx + res.end()] == '.':
        
        sub = parse_members_param(param, idx + res.end() + 1)
        return ({res.group() : sub[0]}, sub[1])
    return ({res.group() : {}}, idx + res.end())

def get_member_base(id, member_names, objects):
    try:
        obj = objects.get(id = id)
    except ObjectDoesNotExist as e:
        return raw_response(-1, f"{id} doesn't exist.")
    return raw_response(1, "ok", get_member_recursive(obj, parse_members_param(member_names)[0]))
def query_base(req, id, objects):
    query_members = req.GET.get('query')
    if query_members == None:
        return try_wrap(lambda: format_raw(get_base(id, objects)))
    return try_wrap(lambda: format_raw(get_member_base(id, query_members, objects)))