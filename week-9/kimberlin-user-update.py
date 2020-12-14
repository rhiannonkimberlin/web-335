"""
============================================
; Title:  kimberlin-user-update.py
; Author: Professor Krasso
; Date:  December 8 2020
; Modified by: Rhiannon Kimberlin
; Description: Updating and Deleting Documents
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
db.users.update_one(
    {"employee_id": "1234567890"},
    {
        "$set" : {
            "email": "rkimberlin@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "1234567890"}, {"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))