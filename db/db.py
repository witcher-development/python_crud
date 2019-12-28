from bson.objectid import ObjectId

address = 'mongodb://localhost:27017'
db_name = 'pymongo_crud'


def add_user(db):
    db.users.insert_one({"name": "Jhon"})


def get_users(db):
    return list(map(lambda user: user, db.users.find()))


def get_user(db, id):
    return db.users.find_one({'_id': ObjectId(id)})

# if __name__ == "__main__":
#     db = get_db()
# add_user(db)
# print(get_users(db))
