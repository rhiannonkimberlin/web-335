"""
============================================
; Title:  kimberlin-user-service.py
; Author: Professor Krasso
; Date:  December 8 2020
; Modified by: Rhiannon Kimberlin
; Description: Querying and Creating Documents 
===========================================
"""

first_name = 'Rhiannon'
last_name = 'Kimberlin'
print(first_name + ' ' + last_name)

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

user = {
    "first_name": "Casimir",
    "last_name": "Basille",
    "email": "casib@me.com",
    "employee_id": "1234567890",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "1234567890"}))