#!/usr/bin/env python3
"""insert records into mongodb database"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert records into mongodb database"""
    item = mongo_collection.insert_one(kwargs)
    return item.inserted_id
