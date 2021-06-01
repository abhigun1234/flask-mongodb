from flask import Flask,request
from dbhelper import get_db
app = Flask(__name__)

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
   return 'hello'
print("__name",__name__)
if __name__ == "__main__":
   app.run()