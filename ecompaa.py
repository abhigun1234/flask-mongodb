from flask import Flask,request
app = Flask(__name__)
from pymongo import MongoClient
def get_db():

    client = MongoClient('localhost:27017')
    db = client.myshop
    return db


def add_products(db,data):
    print("data db helper",data)
    db.product.insert_one(data)


def get_product(db):
    return db.product.find_one()
# basic route
@app.route("/")
def main():
   return 'hello'
@app.route("/api/customer")
def getCustomer():
   return 'hello customer'
@app.route("/add",methods=["POST"])
def add_product():
   db=get_db()
   data=request.get_json()
   print("name",data['name'])
   print("price", data['price'])
   add_products(db,data)
   return 'data inserted'
print("__name",__name__)
if __name__ == "__main__":
   app.run()