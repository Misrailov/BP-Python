from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
now = datetime.now()


def get_database():
    connection_string_mongo = os.getenv("mongo_connection_string")
    client = MongoClient(connection_string_mongo)
    return client["bp_py"]


def create_item(_category, _prompt_length, _prompt, _result, _total_time, _model,_size:str):
    db_name = get_database()
    collection_name = db_name["results"]
    item = {
        "category": _category,
        "prompt_length": _prompt_length,
        "prompt": _prompt,
        "result": _result,
        "total_time": str(_total_time),
        "model": _model,
        "size": _size
    }
    collection_name.insert_one(item)

#create_item("test1", "test1", "test1", "test1")
