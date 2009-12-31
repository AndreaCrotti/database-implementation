#!/usr/bin/env python
# generate the table
# and test it with sqlite/postgresql/mysql
# to check if optimization are actually working or not
# relational algebra operations can be checked using dictionaries and sets

import sqlite3
import random
from itertools import izip

db = "ex10_1.db"
# otherwise I can also use the memory

db_tables = {
    "supplier" : ["id", "place.id", "name"],
    "place" : ["id", "district", "city", "country"],
    "employee" : [ "id", "place.id" , "nationality", "sex", "age" ],
    "gift" : [ "id" , "supplier.id", "name" , "price", "description"],
    "preference" : [ "gift.id" , "employee.id" , "note" ],
    "shipment" : [ "gift.id" , "employee.id" ,  "supplier.id"]
    }

cardinality = {
    "gift" : 6000,
    "employee" : 10000,
    "supplier" : 500,
    "place" : 1000
    }

def gen_db(tables):
    FMT = "CREATE TABLE %s(%s)"
    for t in tables:
        fields = []
        local = False
        for f in db_tables[t]:
            if f == "id":
                local = True
                fields.append(" ".join([f, "PRIMARY KEY"]))
            if f.find(".") > 0:
                # the use the foreign key thing
                pass
        if not local:
            pass
        
# Grammar for indexes: "CREATE INDEX <name> on <TABLE.field>"
# this will be useful later in the query plan to optimize as much as possible

def generate(item):
    return ("item" + "_" + str(x) for x in xrange(cardinality[item]))

# izip together the value to generate the new database

sqltable = gen_db(db_tables.keys())

