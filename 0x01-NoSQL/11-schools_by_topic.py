#!/usr/bin/env python3
"""Query collection by object topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Query collection by object topic"""
    return mongo_collection.find({"topics": topic})
