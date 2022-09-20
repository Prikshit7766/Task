'''1 . Write a program to insert a record in sql table via api
2.  Write a program to update a record via api
3 . Write a program to delete a record via api
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well .'''

from flask import Flask, request, jsonify

# Flask library help you out to expose your function to outer world
# import of flask library
app = Flask(__name__)  # creaed an object  of Flask class ,to use all the function , varibles , methods inside the class


@app.route('/abc', methods=["GET",
                            "POST"])  # act as a decorator and it is trying to decorate the function test1(). here we are going to use url
# Api -- platform independent and to establish communication we use protocol
# api is set of protocol by which you will reach out to a specific system
#
# by using GET and POT  i will be able to  send data to /abc root
# @ is just an annotation i.e after this  what ever function we have always call this function
# GET - posting a data in a URL
# POST - posting a data through a body
def test():  # to reach to this  fuction i have to reach out my system first, once i m inside the system  then i can execute it
    if (request.method == 'POST'):
        # we not passing data , here  we want our postman to pass data for this system
        a = request.json["number1"]  # this value some one suppose to pass  ,, epection  data in json format
        b = request.json["number2"]
        result = a + b
        return jsonify(str(result))  # return in the form of jason


# call this function by using other browser or somewhere else ( browser,postman-- tool to test an api)
# here what we are doing we have a function but we don't want to execute this  function from here ,
# i want to execute this function through postman or other browser


# now we are creatinng second  mwthod
@app.route('/abc1', methods=["GET", "POST"])
# we just ned to chnage route
def test2():
    if (request.method == "POST"):
        a = request.json["number1"]
        b = request.json["number2"]
        result = a * b
        return jsonify(str(result))


# we are calling these function through url not from function name
# simillry we can create as my function we want


if __name__ == '__main__':  # this to invoke the entire python main classes
    # so that i will be able to invoke the main classes

    app.run()  # when we call app.run then the object app that we have created above will avoke

# now go to postman




{
"emp_id":101,
"emp_name" :"c",
"emp_mailid":"prik@gmail.com",
"emp_salary":100,
"emp_attendence":30
 }

if a1 == "emp_name":
    pass
if a1 == "emp_mailid":
    pass
if a1 == "emp_salary":
    pass
if a1 == "emp_attendence":
    pass

