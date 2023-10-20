#!/usr/bin/env python3
"""Update documents in database based on name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Update document in database based on name"""
    mongo_collection.update_many(
            {"name": name},
            {"$set": {'topics': topics}}
            )
