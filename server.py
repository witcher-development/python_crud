from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps

from db.db import address, db_name, get_users, get_user

app = Flask(__name__)
app.config['MONGO_DBNAME'] = db_name
app.config['MONGO_URI'] = address + '/' + db_name
mongo = PyMongo(app)


@app.route('/')
def get_users_route():
    return Response(dumps(get_users(mongo.db)), mimetype='text/json')


@app.route('/user/<id>')
def get_user_route(id):
    return Response(dumps(get_user(mongo.db, id)), mimetype='text/json')


if __name__ == '__main__':
    app.run()
