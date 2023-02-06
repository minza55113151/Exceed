from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
load_dotenv(".env")


username = os.getenv("user")
password = os.getenv("pass")


client = MongoClient(f"mongodb://{username}:{password}@mongo.exceed19.online:8443/?authMechanism=DEFAULT")

db = client["exceed11"]
collection = db["enrollment_system"]

res = collection.insert_many([
    {
        "stdId": 1,
        "stdName": "A",
        "course_name": "Python",
        "grade": 4,
        "unit": 3
    },
    {
        "stdId": 2,
        "stdName": "B",
        "course_name": "Java",
        "grade": 3,
        "unit": 3
    },
    {
        "stdId": 3,
        "stdName": "C",
        "course_name": "C#",
        "grade": 2,
        "unit": 3
    },
    {
        "stdId": 4,
        "stdName": "D",
        "course_name": "C++",
        "grade": 1,
        "unit": 3
    },
    {
        "stdId": 5,
        "stdName": "E",
        "course_name": "JavaScript",
        "grade": 0,
        "unit": 3
    }
])
print(res)