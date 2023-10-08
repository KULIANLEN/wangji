from django.shortcuts import render
from django.core.exceptions import *
from .models import user_data
from common.common import *
from .common import *
from .members import members as user_queries
import re
from .gacha_pool import gacha
import hashlib
import base64
import time

default_pool = {
    1 : 10,
    2 : 8,
    3 : 5,
    101 : 10,
    102 : 1,
    103 : 5,
    201 : 4,
}

# Create your views here.
def query(req, id):
    return query_base(req, id, user_data.objects)

def create(req):
    try:
        req_json = json.loads(req.body)
        user_id = req_json.get("user_id")
        if user_id == None:
            return format_response(-1, "Missing data user_id.")
        if user_data.objects.filter(id = user_id).exists():
            return format_response(-1, f"User {user_id} already exists.")
        ic = gen_code(lambda code: not user_data.objects.filter(user_inv_code = code).exists())
        user = user_data()
        user.id = user_id
        user.user_inv_code = ic
        user.gacha_token = 5
        user.order_token = 2
        user.possessions = [0, 100, 200, 300]
        user.save()
        return format_response(1, "ok")
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}.")

def get_inv_code(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Missing data user_id.")
        return format_response(1, "ok", user.user_inv_code)
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}.")

def claim_inv_code(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Missing data user_id.")
        ic = req_json.get("user_inv_code")
        if ic == None:
            return format_response(-1, "Missing data user_inv_code.")
        if user.invited:
            return format_response(-1, "You have claimed one already.")
        try:
            other = user_data.objects.get(user_inv_code = ic)
            if other == user:
                return format_response(-1, "You cannot invite yourself.")
            other.gacha_token += 5
            user.gacha_token += 3
            user.invited = True
            other.save()
            user.save()
            return format_response(1, "ok", other.id)
        except ObjectDoesNotExist as e:
            return format_response(-1, f"Invalid user invitation code {ic}.")
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}.")

def gacha5(req):
    try:
        
        user = auth(json.loads(req.body))
        if user == None:
            return format_response(-1, "Authentication failed.")
        
        if user.gacha_token <= 0:
            return format_response(-1, "Out of gacha token.")
        
        pool = dict(map(lambda k : (k, default_pool[k]), set(default_pool.keys()).difference(user.possessions)))
        items_get = []
        for i in range(5):
            if len(pool) == 0:
                break
            item = gacha(pool)
            items_get.append(item)
            pool.pop(item)
        user.gacha_token -= 1
        user.possessions += items_get
        user.save()
        return format_response(1, "ok", json.dumps(items_get))
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}")