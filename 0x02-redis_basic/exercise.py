#!/usr/bin/env python3
"""Create a Cache class with redis"""
import redis
import uuid
import typing


class Cache():
    """A Cache class using redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
