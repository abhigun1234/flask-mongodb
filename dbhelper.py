from pymongo import MongoClient
def get_db():

    client = MongoClient('localhost:27017')
    db = client.myshop
    return db


def add_products(db):
    print("data db helper",data)
    db.product.insert_one(data)


def get_product(db):
    return db.product.find_one()
print("__name",__name__)

if __name__ == "__main__":
    db = get_db()
    add_products(db)
    data=get_product(db)
    print("data",data)
    #print()
