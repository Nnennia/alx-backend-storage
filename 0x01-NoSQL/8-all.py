from pymongo.collection import Collection
from typing import List, Dict
#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection"""

def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Lists all documents in a MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection to list documents from.

    Returns:
    List[Dict]: A list of all documents in the collection.
    """
    if mongo_collection is None:
        return []
    documents = mongo_collection.find()
    all_documents = list(documents)
    return all_documents
