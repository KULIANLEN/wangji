from . import models


members={
    "id": lambda order : order.id,
    "owner": lambda order : order.owner.id,
    "items": lambda order : order.items,
    "extra": lambda order : order.extra,
    "complement" : lambda order : None if order.complement == None else order.complement.id,
    "status" : lambda order : order.status,
}