import  logging
logging.basicConfig(filename="except.log", level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
class rand:
    def input_2_integers_and_calculate_division(self):
        while True:

            try:
                logging.info("we are into function")
                a = int(input("write your first number"))
                logging.info("first number entered  %s ",a)
                b = int(input("write your second number"))
                logging.info("second number entered  %s", b)
                c = a / b
                logging.info("result---> %s",c)
                break
            except ValueError:
                logging.info("there should not be string")


            except Exception as e:
                logging.info(e)
                logging.exception(e)

d=rand()
d.input_2_integers_and_calculate_division()