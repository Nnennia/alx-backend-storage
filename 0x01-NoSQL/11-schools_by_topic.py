#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having a specific topic
"""

from typing import List, Dict

def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """
    Return a list of schools that have the specified topic in their topics list.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to search.
        topic (str): The topic to search for.
        
    Returns:
        List[Dict]: A list of schools that have the specified topic in their topics list.
    """
    return list(mongo_collection.find({"topics":  {"$in": [topic]}}))
