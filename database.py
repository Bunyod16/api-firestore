import csv 
import os
from google.cloud import firestore
from utils import COLLECTION

db = firestore.Client()

def add_wallet(wallet, user_id, user_name, date):
    user_id = str(user_id)
    try:
        db = firestore.Client()
        doc_ref = db.collection(COLLECTION).document(user_id)
        doc_ref.set({
            "user_id" : user_id,
            "user_name" : user_name,
            "wallet": wallet,
            "last_updated" : date
        })
    except:
        return (0)
    return (1)

def get_wallet(user_id):
    user_id = str(user_id)
    doc_ref = db.collection(COLLECTION).document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return(doc.to_dict())
    else:
        return (0)

def update_wallet(wallet_address, user_id, date):
    user_id = str(user_id)
    doc_ref = db.collection(COLLECTION).document(user_id)
    doc_ref.update({"wallet":wallet_address, "last_updated":date})
    return (1)   

def db_export_csv():
    users_ref = db.collection(COLLECTION)
    docs = users_ref.stream()
    ls = []
    for doc in docs:
        ls.append(doc.to_dict())

    keys = ls[0].keys()
    with open('whitelist.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(ls)

def db_clear_csv():
        os.system("rm whitelist.csv")

