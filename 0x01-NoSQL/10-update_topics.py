#!/usr/bin/env python3
"""A python function that changes all topics of a school document based on the name"""
from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    """
    Updates the topics of a school document based on the name.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection to update.
    name (str): The name of the school document to update.
    topics (List[str]): The new list of topics to set for the school document.

    Returns:
    pymongo.results.UpdateResult: The result of the update operation.
    """
    return mongo_collection.update_many({
        "name": name
    },
    {
        "$set":{
            "topics": topics
        }
        
    })
