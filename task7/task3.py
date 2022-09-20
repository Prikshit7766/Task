import re
import logging
import pymongo
logging.basicConfig(filename="class.log", level=logging.DEBUG,format=' %(levelname)s %(asctime)s %(name)s  %(message)s')

d = {}
class job_Portal:
    logging.info("you are into job_portal")

    while True:
        __name=input("enter your full name ")
        if len(__name)==0:
            logging.error("you can't leave this field blank")



        else:
            break
    while True:
        __skills =set(input("eneter 5 unique  skills sepreated by coma").split(","))

        print(__skills)
        if len(__skills)==5:
            break

        else:
            logging.error("plz eneter only 5 skills seprated by coma ")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


    while True:
        __email=input("provide a valid enamil")



        if(re.fullmatch(regex,__email)):
            break

        else:
            logging.error("plz eneter the valid eamil")

    def ineuron_record(self):
        f = open('ineuron_record.txt', "a")
        print(str(job_Portal.__name),str(job_Portal.__skills),str(job_Portal.__email))
        f.write(str(job_Portal.__name)+"\n")

        f.write(str(job_Portal.__skills)+"\n")
        f.write(str(job_Portal.__email)+"\n")
        f.write("-----------------------------------------------")
        f.close()
    def convert_record_to_dict(self):

        d["name"]=job_Portal.__name
        d["skills"]=job_Portal.__skills
        d["email"]=job_Portal.__email
        print(d.items())


    def insert_record_to_mogodb(self):
        client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@cluster0.bb7u7jb.mongodb.net/?retryWrites=true&w=majority")
        db = client.test

        database = client["ineuron_record"]
        collection = database["record"]
        collection.insert_one(d)









a=job_Portal()
a.ineuron_record()
a.convert_record_to_dict()
a.insert_record_to_mogodb()
