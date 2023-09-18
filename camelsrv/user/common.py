from .models import *
from django.core.exceptions import *
def auth(req_json):
    print(req_json)
    id = req_json["user_id"]
    if id == None:
        return None
    try:
        return user_data.objects.get(id = id)
    except ObjectDoesNotExist as e:
        return None
