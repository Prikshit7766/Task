import logging
logging.basicConfig(filename="class.log", level=logging.DEBUG,format=' %(levelname)s %(asctime)s %(name)s  %(message)s')

class subject:
    __l_course = ["Aptitude", "Big Data", "Cloud", "Cyber Security", "Data Analytics", "Data Science", "Data Structure",
                "Database", "DevOps", "Digital Marketing", "Drone", "Hardware", "IOT", "Mobile Development",
                "Programming", "RPA", "Salesforce", "System Design", "Testing", "Web Development", "Blockchain"]
    __one_pakage = ["Tech Neuron", "Kids Neuron"]


class select_cource(subject):
    logging.info("i m in the course section")


    def cources(self,c):
        logging.info("these are the cources %s",c)
        l=[]

        n=[]
        while True:

                a= str(input("which cources you want to take "))
                l.append


                if a in c:
                    info_1 = input("enter your name")
                    n.append(info_1)
                    info_2 = input("enter your email")
                    n.append(info_2)

                    logging.info("name -> %s  email -> %s  course you have selected --> %s", n[0], n[1], a)

                    b = input("do you want to add one more course enter -> yes")
                    if b=="yes":
                        continue
                    else:

                        break
                else:

                      logging.error("invalid choice ")

        return l,n


    def One_Neuron(self,oc):
        n = []
        while True:
            a=input("which option you want to select ")
            if a in oc:
                info_1 = input("enter your name")
                n.append(info_1)
                info_2 = input("enter your email")
                n.append(info_2)

                logging.info("name -> %s  email -> %s  course you have selected --> %s", n[0], n[1], a)
                break
            else:


                logging.error("invalid choice ")












i=subject()
couse_select=select_cource()

couse_select.cources(i._subject__l_course )
couse_select.One_Neuron(i._subject__one_pakage)



