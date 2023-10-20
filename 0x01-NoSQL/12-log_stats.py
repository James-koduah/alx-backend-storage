#!/usr/bin/env python3
"""Engage with database of nginx logs"""
import pymongo

def logs():
    """Engage with database of nginx logs"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    database = client.logs.nginx
    
    print("{} logs".format(database.count_documents({})))
    print('Methods:')
    print('\tmethod GET: {}'.format(database.count_documents({'method': 'GET'})))
    print('\tmethod POST: {}'.format(database.count_documents({'method': 'POST'})))
    print('\tmethod PUT: {}'.format(database.count_documents({'method': 'PUT'})))
    print('\tmethod PATCH: {}'.format(database.count_documents({'method': 'PATCH'})))
    print('\tmethod DELETE: {}'.format(database.count_documents({'method': 'DELETE'})))
    print("{} status check".format(database.count_documents({'method': 'GET', 'path': '/status'})))


if __name__ == '__main__':
    logs()
