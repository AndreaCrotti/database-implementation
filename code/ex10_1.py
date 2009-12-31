#!/usr/bin/env python
# generate the table
# and test it with sqlite/postgresql/mysql
# to check if optimization are actually working or not
# relational algebra operations can be checked using dictionaries and sets

import sqlite3
import random

db_file = "ex10_1.db"
# otherwise I can also use the memory
cursor = sqlite3.connect(db_file)

db_tables = {
    "place" : ["id", "district", "city", "country"],
    "supplier" : ["id", "place.id", "name"],
    "employee" : [ "id", "place.id" , "nationality", "sex", "age" ],
    "gift" : [ "id" , "supplier.id", "name" , "price", "description"],
    "preference" : [ "gift.id" , "employee.id" , "note" ],
    "shipment" : [ "gift.id" , "employee.id" ,  "supplier.id"]
    }

cardinality = {
    "gift" : 6000,
    "employee" : 10000,
    "supplier" : 500,
    "place" : 1000,
    "nationalities" : 50
    }

def gen_db(tables):
    FMT = "CREATE TABLE %s(%s);"
    tabs = []
    for t in tables:
        fields = []
        local = False
        for f in db_tables[t]:
            if f == "id":
                local = True
                fields.append(" ".join([f, "PRIMARY KEY"]))
            elif f.find(".") > 0:
                # the use the foreign key thing
                fields.append(" ".join([f.split(".")[0], "FOREIGN KEY REFERENCES %s" % f]))
            else:
                fields.append(f)
        if not local:
            # then the key is a combinantion of the references
            pass
        tabs.append(FMT % (t, ", ".join(fields)))
    return tabs

# Grammar for indexes: "CREATE INDEX <name> on <TABLE.field>"
# this will be useful later in the query plan to optimize as much as possible

def generate(item, card):
    return (item + "_" + str(x) for x in xrange(card))


sex = lambda: random.choice(('m', 'f'))
age = lambda: random.choice(range(18,40))
# is this enough for uniformly distributed stuff?
price = lambda: random.choice(range(11, 210))

nationalities = list(generate("nat", cardinality["nationalities"]))
# there are 50 different nationalities
nationality = lambda: random.choice(nationalities)
# then every employee gets a shipment from where he comes from

# in plus all the cities have same number of employees and more


# query that need optimization
query = """
   SELECT gift.name, supplier.name, COUNT(*)
   FROM gift, supplier, shipment
   WHERE shipment.gift = gift.id AND shipment.supplier = supplier.id
   AND gift.price > 190 AND supplier.place IN
   (SELECT DISTINCT place.id
   FROM employee, place
   WHERE employee.place = place.id AND employee.nationality = 'German' )
   GROUP BY gift.name, supplier.name
"""

sqltable = gen_db(db_tables.keys())
