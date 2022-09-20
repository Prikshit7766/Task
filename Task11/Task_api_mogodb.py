from flask import  Flask ,request, jsonify
import mysql.connector as conn
import pymongo

app = Flask(__name__)

@app.route('/abc1', methods=["GET", "POST"])
def insert_record():
    if (request.method == 'POST'):
        data=request.json["data"]
        client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@cluster0.bb7u7jb.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        database = client["task11"]
        collection = database["ineuron"]
        collection.insert_many(data)
        return ("done")










if __name__ == '__main__':
    app.run()
