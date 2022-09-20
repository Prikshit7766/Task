import  logging
logging.basicConfig(filename="all_.log", level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
class all:
    logging.info("we have entered the all_list class")
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def reverse_list(self):

        logging.info("reverse_list  ---> %s",self.l1[::-1])
    def access_234(self):
        logging.info("access_234  ---> %s",self.l1[7][0])
    def access_456(self):
        logging.info("access_456  ---> %s",self.l1[5][1])
    def extract_only_a_list(self):
        logging.info("extract_only_a_list  ---> %s",self.l1[5:7])
    def extract_sudh(self):
        logging.info("extract_sudh  ---> %s",self.l1[-1]["key1"])
    def list_all_the_key_in_dict(self):
        logging.info("list_all_the_key_in_dict ---> %s",self.l1[-1].keys())
    def extract_all_value_form_dict(self):
        logging.info("extract_all_value_form_dict  ---> %s",self.l1[-1].keys())


    def extract_all_the_list_entity(self):
        count = 1
        for i in self.l2:
            if type(i) == list:
                logging.info("list  %s ----->%s ",count,i )
                count += 1

    def  to_extract_all_the_dict(self):
        count = 1
        for i in self.l2:
            if type(i) == dict:
                l=i.items()
                logging.info("dictionary %s -----> %s", count, i.items())

                count += 1

    def extract_all_the_tuples_entities(self):
        count = 1
        for i in self.l2:
            if type(i) == tuple:

                logging.info("tuple %s -----> %s ",count,i)

                count += 1
    def  extract_all_the_numerical_data_and_summation(self):
        a = []
        for i in self.l2:
            if type(i) == int or type(i) == float:
                a.append(i)
            elif type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int or type(j) == float:
                        a.append(j)
            elif type(i) == dict:
                for j in i.items():
                    if type(j[0]) == int or type(j[0]) == float:
                        a.append(j[0])
                    if type(j[1]) == int or type(j[1]) == float:
                        a.append(j[1])
        logging.info("all the numerical data %s", a)
        logging.info("length----------> %s",len(a))
        logging.info("summation of all the numeric data --------------->%s",sum(a))


    def filter_out_all_the_odd_values_out_all_numeric_data(self):
        c = []
        for i in self.l2:

            if type(i) == list:
                for j in i:
                    if type(j) == int or type(j) == float:
                        c.append(j)

        logging.info("all the numerical data in the list %s", c)
        logging.info("length----------> %s", len(c))


        n = []
        for i in c:
            if i % 2 != 0:
                n.append(i)
        logging.info("odd values out all numeric data---------> %s", n)


    def  extract_ineruon_out_of_this_data(self):
        b = []
        for i in self.l2:
            if type(i) == str and i == "ineuron":

                b.append(i)
            elif type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == str and j == "ineuron":
                        b.append(j)

            elif type(i) == dict:
                for j in i.items():
                    if type(j[0]) == str and j[0] == "ineuron":
                        b.append(j[0])
                        print("scjsbc")
                    if type(j[1]) == str and j[1] == "ineuron":
                        b.append(j[1])
        logging.info("extract ineruon %s", b)
        logging.info("length----------> %s", len(b))

    def find_out_a_number_of_occurances_of_all_the_data(self):
        d = []
        for i in self.l2:
            if type(i) == int:
                d.append(i)
            elif type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    d.append(j)
            elif type(i) == dict:
                for j in i.items():
                    d.append(j[0])

                    d.append(j[1])
        logging.info("all the data %s", d)
        logging.info("length----------> %s", len(d))

        set_d = set(d)
        for i in set_d:
            logging.info("%s occured %s times",i, d.count(i))


    def find_out_number_of_keys_in_dict_element(self):
        e = []
        for i in self.l2:
            if type(i) == dict:
                for j in i.items():
                    e.append(j[0])


        logging.info("keys in dict element %s",e)
        logging.info("length----------> %s", len(e))
    def filter_out_all_the_string_data(self):
        f = []
        for i in self.l2:
            if type(i) == str:
                f.append(i)
            elif type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == str:
                        f.append(j)
            elif type(i) == dict:
                for j in i.items():
                    if type(j[0]) == str:
                        f.append(j[0])
                    if type(j[1]) == str:
                        f.append(j[1])
        logging.info("all the string data %s",f)
        logging.info("length----------> %s", len(f))

    def  Find_out_alphanum_in_data(self):

        d = []
        for i in self.l2:
            if type(i) == int:
                d.append(i)
            elif type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    d.append(j)
            elif type(i) == dict:
                for j in i.items():
                    d.append(j[0])

                    d.append(j[1])
        logging.info("all the data %s",d)
        logging.info("length----------> %s", len(d))

        z = []
        for i in d:
            if type(i) == str:
                if i.isalnum() == True:
                    z.append(i)
        logging.info("alphanum in data %s",z)
        logging.info("length----------> %s", len(z))

    def multiplication_of_all_numeric_value_in_the_individual(self):
        p = []
        q = []
        r = []
        s = []
        t = []
        for i in self.l2:
            if type(i) == int or type(i) == float:
                p.append(i)
            elif type(i) == list:
                for j in i:
                    if type(j) == int or type(j) == float:
                        q.append(j)
            elif type(i) == tuple:
                for j in i:
                    if type(j) == int or type(j) == float:
                        r.append(j)
            elif type(i) == set:
                for j in i:
                    if type(j) == int or type(j) == float:
                        s.append(j)
            elif type(i) == dict:
                for j in i.items():
                    if type(j[0]) == int or type(j[0]) == float:
                        t.append(j[0])
                    if type(j[1]) == int or type(j[1]) == float:
                        t.append(j[1])
        logging.info("numeric value %s",p)

        product = 1

        for x in p:
            product *= x
        logging.info("product------> %s",product)
        logging.info("sum------> %s", sum(p))

        logging.info("numeric value in list  %s ", q)




        product = 1
        for x in q:
            product *= x
        logging.info("product------> %s", product)
        logging.info("sum------> %s", sum(q))

        logging.info("numeric value in tuple  %s ", r)

        product = 1
        for x in r:
            product *= x
        logging.info("product------> %s", product)
        logging.info("sum------> %s", sum(r))

        logging.info("numeric value in set  %s ", s)

        product = 1
        for x in s:
            product *= x
        logging.info("product------> %s", product)
        logging.info("sum------> %s", sum(s))

        logging.info("numeric value in dictionary  %s ", t)

        product = 1
        for x in t:
            product *= x
        logging.info("product------> %s", product)
        logging.info("sum------> %s", sum(t))

    def create_a_flat_list(self):
         d = []
         for i in self.l2:
             if type(i) == int:
                 d.append(i)
             elif type(i) == list or type(i) == tuple or type(i) == set:
                 for j in i:
                     d.append(j)
             elif type(i) == dict:
                 for j in i.items():
                     d.append(j[0])

                     d.append(j[1])
         logging.info("all the data %s", d)
         logging.info("length----------> %s", len(d))








l=all([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}] ,
           [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
#task 2 list
l.reverse_list()
l.access_234()
l.access_456()
l.extract_only_a_list()
l.extract_sudh()
l.list_all_the_key_in_dict()
l.extract_all_value_form_dict()



# task 3 list
l.extract_all_the_list_entity()
l.to_extract_all_the_dict()
l.extract_all_the_tuples_entities()
l.extract_all_the_numerical_data_and_summation()
l.filter_out_all_the_odd_values_out_all_numeric_data()
l.extract_ineruon_out_of_this_data()
l.find_out_a_number_of_occurances_of_all_the_data()
l.find_out_number_of_keys_in_dict_element()
l.filter_out_all_the_string_data()
l.Find_out_alphanum_in_data()
l.multiplication_of_all_numeric_value_in_the_individual()
l.create_a_flat_list()
