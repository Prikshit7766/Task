import mysql.connector as conn
import xlrd

mydb =conn.connect(host="localhost",user="root",passwd="Prikshit@12",db='task8')

cursor= mydb.cursor()

excel_sheet=xlrd.open_workbook(r"D:\full_stack\material\July24\data fsds\Attribute DataSet.xlsx")
excel_sheet
sheet_name=excel_sheet.sheet_names()
sheet_name

insert_query="insert into product details(Dress_ID ,Style ,Price ,Rating ,Size ,Season ,NeckLine ,SleeveLength ,waiseline ,Material ,FabricType ,Decoration ,`Pattern Type` ,Recommendation )values(%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,)"
s2=cursor.execute("""LOAD DATA LOCAL infile 'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Attribute DataSet.csv' INTO TABLE ineuron1 FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY "\n" IGNORE 1 ROWS """)

for  sh in range (0,len(sheet_number)):
