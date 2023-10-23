#!/usr/bin/env python3
"""Create a Cache class with redis"""
import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    key = method.__qualname__
    @wraps(method)
    def wrap(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrap

def call_history(method: typing.Callable) -> typing.Callable:
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"
    
    @wraps(method)
    def wrap(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(res))
        return res
    return wrap


class Cache():
    """A Cache class using redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: typing.Optional[typing.Callable] = None) -> typing.Union[
                    str, bytes, int, float]:
        value = self._redis.get(key)
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        return self.get(key, int)
