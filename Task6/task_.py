# pattern question
import  logging
logging.basicConfig(filename="pattern.log",level=logging.INFO,format="'%(levelname)s %(asctime)s %(name)s  %(message)s")
class Pattern:
    def p1(self):
        n = 4
        for i in range(n + 1):
            print("ineruon " * (i))


    def p2(self):
        n = 3
        z = n
        s = n
        for i in range(n):
            for j in range(i, n - 1):
                print(" " * (len("ineruon") // 2), end=" ")
            for j in range(i + 1):
                print("ineruon", end=" ")
            for j in range(i - z):
                print("ineruon", end=" ")
            print()

        for i in range(n):
            for j in range(n, s - 1, -1):
                print(" " * (len("ineruon") // 2), end=" ")
            for j in range(s, 1, -1):
                print("ineruon", end=" ")
            print()
            s -= 1
    def p3(self):
        a = 1
        b = 9
        z = 1
        while a <= b:
            c = 0
            while z > c:
                print("*", end=" ")
                c += 1
            print()
            a += 1
            z = a
    def p4(self):
        a1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 1
        a = 7
        print(a1[0])
        while i < a:

            print(a1[i], end=" ")
            y = i
            d = 0
            c = i
            add = 6

            while y > d:
                c = c + add
                if len(a1) > c:
                    print(a1[c], end=" ")
                d += 1
                add -= 1
            print()
            i += 1




p=Pattern()
p.p1()
print("")
p.p2()
print("")
p.p3()
print()
p.p4()

