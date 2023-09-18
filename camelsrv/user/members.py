from camelorder import models as camelorder_models
from camelorder.members import members as order_queries
members={
    "id": lambda user : user.id,
    "gacha_token": lambda user : user.gacha_token,
    "order_token": lambda user : user.order_token,
    "possessions": lambda user : user.possessions,
    "orders" : lambda user : list(map(lambda e : order_queries['id'](e), camelorder_models.camel_order.objects.filter(owner=user)))
}