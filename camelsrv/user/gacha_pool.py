import bisect
import random


def gacha(pool):
    total = sum(pool.values())
    ra = random.uniform(0, total)
    curr_sum = 0
    ret = None
    keys = pool.keys()
    for k in keys:
        curr_sum += pool[k]
        if ra <= curr_sum:
            ret = k
            break
    return ret