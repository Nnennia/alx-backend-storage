#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new school document in the given MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Keyword arguments representing the fields of the school document.

    Returns:
        The _id of the inserted document.
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
