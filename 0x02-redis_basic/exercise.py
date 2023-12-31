#!/usr/bin/env python3
"""Create a Cache class with redis"""
import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """save number of times a function or method has been called to redis"""
    key = method.__qualname__
    @wraps(method)
    def wrap(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrap


def call_history(method: typing.Callable) -> typing.Callable:
    """Save the inputs and outputs given to functions or methods to redis"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrap(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(res))
        return res
    return wrap


def replay(method: typing.Callable):
    """Get information about number of times a method has been called"""
    key = method.__qualname__
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    cls = method.__self__
    print("{} was called {} times:".format(key, cls.get_int(key)))

    inputs = cls._redis.lrange(input_key, 0, -1)
    outputs = cls._redis.lrange(output_key, 0, -1)

    for item in list(zip(inputs, outputs)):
        print("{}(*{}) -> {}".format(
              key,
              item[0].decode("utf-8"),
              item[1].decode("utf-8")
              ))


class Cache():
    """A Cache class using redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """store a value with a random generated key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: typing.Optional[typing.Callable] = None) -> typing.Union[
                    str, bytes, int, float]:
        """get value from redis database"""
        value = self._redis.get(key)
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """encapsulates the get function"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """encapsulates the get function"""
        return self.get(key, int)
