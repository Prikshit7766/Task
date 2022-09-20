import mysql.connector as conn

mydb =conn.connect(host="localhost",user="root",passwd="Prikshit@12")

cursor= mydb.cursor()
s=cursor.execute("create table if not exists task8.ineuron1(Dress_ID int,Style varchar(40),Price varchar(40),Rating float,Size varchar(4),Season varchar(40),NeckLine varchar(40),SleeveLength varchar(40),waiseline varchar(40),Material varchar(40),FabricType varchar(40),Decoration varchar(40),`Pattern Type` varchar(40),Recommendation int(1))")

s1=cursor.execute("create table if not exists task8.ineuron2(Dress_ID int,`29/8/2013` int,`31/8/2013` int,`2013-02-09 00:00:00` int,`2013-04-09 00:00:00` int,`2013-06-09 00:00:00` int,`2013-08-09 00:00:00` int,`2013-10-09 00:00:00` int,`2013-12-09 00:00:00` int,`14/9/2013` int,`16/9/2013` int,`18/9/2013` int,`20/9/2013` int,`22/9/2013` int,`24/9/2013` int,`26/9/2013` int,`28/9/2013` int,`30/9/2013` int,`2013-02-10 00:00:00` int,`2013-04-10 00:00:00` int,`2013-06-10 00:00:00` int,`2010-08-10 00:00:00` int,`2013-10-10 00:00:00` int,`2013-12-10 00:00:00` int)")