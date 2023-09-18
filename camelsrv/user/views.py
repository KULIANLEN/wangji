from django.shortcuts import render
from django.core.exceptions import *
from . import models
from common.common import *
from .members import members as user_queries
import re

item_pool={
    1:1,
    2:3
}
weight_sum = 0
for v in item_pool.values():
    weight_sum += v


# Create your views here.
def query(req, id):
    return query_base(req, id, user_queries, models.user_data.objects, "user")
def query_member(req, id, member_name):
    return query_member_base(id, member_name, user_queries, models.user_data.objects, "user")
def gacha5(req):
    return