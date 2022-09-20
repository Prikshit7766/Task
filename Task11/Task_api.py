from flask import  Flask ,request, jsonify
import mysql.connector as conn

import pymongo


app = Flask(__name__)


@app.route('/abc123', methods=["GET", "POST"])


def insert_record():
    if (request.method == 'POST'):


        mydb = conn.connect(host="localhost", user="root", passwd="1234")
        cursor = mydb.cursor()

        a1 = request.json["emp_id"]
        a2 = request.json["emp_name"]
        a3 = request.json["emp_mailid"]
        a4 = request.json["emp_salary"]
        a5 = request.json["emp_attendence"]

        s=f"insert into Task_api.ineuron VALUES ({a1},'{a2}','{a3}',{a4},{a5})"
        s=cursor.execute(s)
        mydb.commit()
        return("done")
@app.route('/abc1234', methods=["GET", "POST"])
def update_record():
    if(request.method == 'POST'):
        mydb = conn.connect(host="localhost", user="root", passwd="1234")
        cursor = mydb.cursor()
        c1 = request.json["c1"]
        c2 = request.json["c2"]
        v1 = request.json["v1"]
        v2 = request.json["v2"]
        o=request.json["o"]
        if type(v1)==int and type(v2) ==int:
            s = f"UPDATE Task_api.ineuron set {c1} {o} {v1} where {c2} {o} {v2}"
            s = cursor.execute(s)
            mydb.commit()

            return ("done")
        elif (type(v1)== str  and  type(v2) ==int):
            s=f"UPDATE Task_api.ineuron set {c1} {o} '{v1}' where {c2} {o} {v2} "
            s = cursor.execute(s)
            mydb.commit()
            return ("done")

        elif (type(v1)== int  and  type(v2) ==str):
            s=f"UPDATE Task_api.ineuron set {c1} {o} {v1} where {c2} {o} '{v2}' "
            s = cursor.execute(s)
            mydb.commit()

            return ("done")

        elif (type(v1) == str and type(v2) == str):
            s=f"UPDATE Task_api.ineuron set {c1} {o} '{v1}' where {c2} {o} '{v2}' "
            s = cursor.execute(s)
            mydb.commit()

            return ("done")


@app.route('/abc12345', methods=["GET", "POST"])
def delete_record():

    if (request.method == 'POST'):
        mydb = conn.connect(host="localhost", user="root", passwd="1234")
        cursor = mydb.cursor()
        c1= request.json["c1"]
        v1= request.json["v1"]
        o = request.json["o"]
        if type(v1)==int:

            s=f"DELETE FROM Task_api.ineuron  where {c1} {o} {v1} "
            s = cursor.execute(s)
            mydb.commit()
            return ("done")
        if type(v1) == str:
            s = f"DELETE FROM Task_api.ineuron  where {c1} {o} '{v1}' "
            s = cursor.execute(s)
            mydb.commit()

            return ("done")


@app.route('/abc123456', methods=["GET", "POST"])
def fetch_record():
    if (request.method == 'POST'):
        mydb = conn.connect(host="localhost", user="root", passwd="1234")
        cursor = mydb.cursor()
        cursor.execute("select * from   Task_api.ineuron")
        l = []
        for i in cursor.fetchall():
            l.append(i)

        return (l)



# or with query in postman
@app.route('/abc1', methods=["GET", "POST"])
def insert_record1():
    if (request.method == 'POST'):
        mydb = conn.connect(host="localhost", user="root", passwd="1234")
        cursor = mydb.cursor()

        a1 = request.json["a"]

        cursor.execute(a1)
        mydb.commit()
        return ("done")

@app.route('/abc1234567', methods=["GET", "POST"])
def insert_record_mogodb():
    if (request.method == 'POST'):
        url = request.json["url"]
        data=request.json["data"]


        client = pymongo.MongoClient(url)
        db = client.test

        database = client["task11"]
        collection = database["ineuron"]
        collection.insert_many(data)
        return ("done")


@app.route('/abc12345678', methods=["GET", "POST"])
def update_record_mogodb():
    if (request.method == 'POST'):
        url = request.json["url"]



        client = pymongo.MongoClient(url)
        db = client.test

        database = client["task11"]
        collection = database["ineuron"]
        c1 = request.json["c1"]
        c2 = request.json["c2"]
        v1 = request.json["v1"]
        v2 = request.json["v2"]

        collection.update_one({f"{c2}":f"{v2}"},{"$set":{f"{c1}":f"{v1}"}})
        return ("done")


@app.route('/abc123456789', methods=["GET", "POST"])
def delete_record_mogodb():
    if (request.method == 'POST'):
        url = request.json["url"]



        client = pymongo.MongoClient(url)
        db = client.test
        database = client["task11"]
        collection = database["ineuron"]
        c1 = request.json["c1"]
        v1 = request.json["v1"]
        collection.delete_one({f"{c1}":f"{v1}"})
        return ("done")


@app.route('/abc1234567891', methods=["GET", "POST"])
def fetch_record_mogodb():
    if (request.method == 'POST'):
        url = request.json["url"]

        client = pymongo.MongoClient(url)
        db = client.test
        database = client["task11"]
        collection = database["ineuron"]
        record = collection.find()

        r=list(record)

        return str(r)







if __name__ == '__main__':
    app.run(port=8000)
