#!/usr/bin/env python3
"""Obtain HTML content from a url and return it"""
import redis
import requests
r = redis.Redis()

def get_page(url: str) -> str:
    """get an html page"""
    cache = r.get(f"cache:{url}")
    if cache:
        return cache.decode('utf-8')
    html = requsts.get(url).text
    r.incr(f"count:{url}")
    r.setex(f"cache:{url}", 10, html)
    return html
