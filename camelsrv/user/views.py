from django.shortcuts import render
from django.core.exceptions import *
from .models import user_data
from common.common import *
from .common import *
from .members import members as user_queries
import re
from .gacha_pool import gacha

default_pool = {
    10 : 10,
    11 : 8,
    12 : 5,
    13 : 10,
    14 : 1,
    15 : 5,
    16 : 4,
}

# Create your views here.
def query(req, id):
    return query_base(req, id, user_data.objects)
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