
import mysql.connector as conn
mydb =conn.connect(host="localhost",user="root",passwd="1234")
cursor= mydb.cursor()
#cursor.execute("create database Task_api")
#cursor.execute("show databases")
s=cursor.execute("create table Task_api.ineuron (emp_id int(10),emp_name varchar(40),emp_mailid varchar(30), emp_salary int(6), emp_attendence int(3))")
q1=cursor.execute(s)

q2= cursor.execute("select * from Prikshit.ineuron1")
print(q2)
