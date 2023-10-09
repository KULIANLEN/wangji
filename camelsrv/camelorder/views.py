from django.shortcuts import render
from django.core.exceptions import *
from .models import *
from user.models import *
from .members import members as order_queries
from common.common import *
from user.common import *
import json
import hashlib
import base64
import time
# Create your views here.
def query(req, id):
    return query_base(req, id, camel_order.objects)
def create(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Authentication failed.")
        if user.order_token <= 0:
            return format_response(-1, "Out of order token.")
        order = camel_order()
        order.owner = user
        ic = req_json.get('cp_inv_code')
        order.status = 0
        order.items={"head":0, "face": 100, "neck": 200, "seat": 300}
        order.extra={"name": "骆驼酱"}
        if ic != None:
            try:
                ic = cp_inv_code.objects.get(code = ic)
                if ic.order.status != 1:
                    return format_response(-1, f"{ic} isn't a valid complement invitation code.")
                if ic.order.owner == user:
                    return format_response(-1, f"You are attempting to pair with yourself.")
            except:
                return format_response(-1, f"{ic} isn't a valid complement invitation code.")
            order.complement = ic.order
            order.save()
            ic.order.complement = order
            ic.order.status = 0
            ic.order.save()
            ic.delete()
        user.order_token -= 1
        user.save()
        order.save()
        return format_response(1, "ok", order.id)
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}")
def create_cp(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Authentication failed.")
        if user.order_token <= 0:
            return format_response(-1, "Out of order token.")
        order = camel_order()
        order.owner = user
        order.items={"head":0, "face": 100, "neck": 200, "seat": 300}
        order.extra={"name": "骆驼酱"}
        user.order_token -= 1
        ic = cp_inv_code()
        ic.code = gen_code(not cp_inv_code.objects.filter(code = ic.code).exists())
        order.status = 1
        order.save()
        ic.order = order
        ic.save()
        user.save()
        return format_response(1, "ok", {"order_id": order.id, "cp_inv_code": ic.code})
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}")
def delete(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Authentication failed.")
        order = req_json.get('order_id')
        if order == None:
            return format_response(-1, "Missing data order_id.")
        try:
            order = camel_order.objects.get(id = int(order))
        except Exception as e:
            return format_response(-1, f"Invalid order_id parameter: {order}")
        if order.owner != user:
            return format_response(-1, f"Order {order.id} doesn't belong to user {user.id}.")
        order.delete()
        user.order_token += 1
        user.save()
        return format_response(1, "ok")
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}")
def modify(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Authentication failed.")
        
        try:
            order = req_json.get('order_id')
            if order == None:
                return format_response(-1, "Missing data order_id.")
            order = camel_order.objects.get(id = int(order))
        except:
            return format_response(-1, f"Invalid order_id parameter: {order}.")
        if order.status != 0:
            return format_response(-1, f"Order {order.id} is now on status {order.status}, you can only modify orders on status 0.")
        if user != order.owner:
            return format_response(-1, f"Order {order.id} doesn't belong to {user.id}.")
        available_items = set(user.possessions)
        if order.complement != None:
            available_items.update(order.complement.owner.possessions)
        items = req_json.get('items')
        if items != None:
            for v in items.values():
                if not v in available_items:
                    return format_response(-1, f"Items parameter containing unavailable item(s).")
            order.items = items
        extra = req_json.get('extra')
        if extra != None:
            order.extra = extra
        order.save()
        return format_response(1, "ok")
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}")
def submit(req):
    try:
        req_json = json.loads(req.body)
        user = auth(req_json)
        if user == None:
            return format_response(-1, "Authentication failed.")
        try:
            order = req_json.get('order_id')
            if order == None:
                return format_response(-1, "Missing data order_id.")
            order = camel_order.objects.get(id = int(order))
        except:
            return format_response(-1, f"Invalid order_id parameter: {order}.")
        if order.status != 0:
            return format_response(-1, f"Order {order.id} is now on status {order.status}, you can only modify orders on status 0.")
        if user != order.owner:
            return format_response(-1, f"Order {order.id} doesn't belong to {user.id}.")
        order.status = 2
        order.save()
        return HttpResponse(1, "ok")
    except Exception as e:
        return format_response(-1, f"Server error: {str(e)}")
def obtain_submitted(req):
    ret = []
    for e in camel_order.objects.filter(status = 2):
        toAdd = {}
        for k, v in e.query_methods().items():
            toAdd[k] = try_deref(v(), wild(wild({})))
        ret.append(toAdd)
    return format_response(1, "ok", json.dumps(ret))