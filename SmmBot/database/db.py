from tinydb import TinyDB, Query
from tinydb.database import Document
from pprint import pprint
import json
User = Query()

db1=TinyDB('database/users.json', indent=4)
db2=TinyDB('database/medias.json', indent=4)
products  = db2.table('media') 

users     = db1.table('Users')
index     = db1.table('Index')

def get(table=None, user_id=None, media_id=None, uniq_id=None):


    if table == "users":
        if user_id == None:
            return users.all()
        else:
            return users.get(doc_id=user_id)
    elif table == "index":
        return index.get(doc_id=user_id)
    
    elif table == "media":
        tip = Query()
        return db2.search(tip.media_type == media)
    
def insert(table, data, user_id=None, media_type=None):
    if table == "users":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        users.insert(doc)
    
    elif table == "index":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        index.insert(doc)

    # elif table == "media":
    #    doc_id = db2.insert(data)
    #    return doc_id
    
def upd(table, data, user_id=None, media=None):

    if table == "index":
        index.update(data, doc_ids=[user_id])
    # if table == "media":
    #     user_ids = int(get(table="index", user_id=user_id)['edit_doc'])
    #     db2.update(data, doc_ids=[user_ids])