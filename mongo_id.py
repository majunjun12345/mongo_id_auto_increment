#coding:utf-8


from pymongo import MongoClient
from pymongo import ReturnDocument
# ReturnDocument.AFTER
# ReturnDocument.BEFORE

client = MongoClient("127.0.0.1", 27017)

db = client.test

user_collection = db.user
id_collection = db.id

def id_base_insert():
    id_collection.insert({"name":"user", "id":0})
    return


def add_user():
    userid = id_collection.find_one_and_update({"name": "user"}, {"$inc": {"id": 1}}, return_document=ReturnDocument.AFTER)
    print "userid:%s" % userid
    user_collection.save({"_id":userid["id"], "username":"dotcoo", "password":"dotcoo", "info":"http://www.dotcoo.com/"})
    return userid


def user():
    users = []
    user = user_collection.find()
    for u in user:
        users.append(u)
    return users, len(users)

if __name__ == "__main__":
    # id_base_insert()
    add_user()
    user()


