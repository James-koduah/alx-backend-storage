#!/usr/bin/env python3
"""Obtain HTML content from a url and return it"""
import redis
import requests
from functools import wraps
r = redis.Redis()


def cache_get_page(func):
    @wraps(func)
    def wrap(url: str):
        old_cache = r.get(f"cache:{url}")
        if old_cache:
            return old_cache.decode("utf-8")

        new_cache = func(url)
        r.setex(f'cache:{url}', 10, new_cache)
        return new_cache
    return wrap

@cache_get_page
def get_page(url: str) -> str:
    """get an html page"""
    r.incr(f"count:{url}")
    html = requests.get(url).text
    return html
