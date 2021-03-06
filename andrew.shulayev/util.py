#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import ceil

def unzip(*args):
    return list(zip(*args))

def split(ls, parts):
    n = len(ls)
    part_size = int(ceil(n / parts))
    for i in range(parts):
        yield ls[i * part_size:(i + 1) * part_size]

def append(args):
    result = []
    for ls in args:
        result.extend(ls)
    return result

def average(ls):
    if len(ls) == 0:
        return 0
    return sum(ls) / len(ls)