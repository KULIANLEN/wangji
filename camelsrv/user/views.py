from django.shortcuts import render
from django.core.exceptions import *
from . import models
from common.common import *
from .members import members as user_queries

import re


# Create your views here.
def query(req, id):
    return query_base(req, id, user_queries, models.user_data.objects, "user")
def query_member(req, id, member_name):
    return query_member_base(id, member_name, user_queries, models.user_data.objects, "user")