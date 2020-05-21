'''cells = input("Enter cells:")
print("---------")
print("|", cells[0], cells[1], cells[2], "|")
print("|", cells[3], cells[4], cells[5], "|")
print("|", cells[6], cells[7], cells[8], "|")
print("---------")'''
from math import e

e = 1


def func_1():
    e = 0

    def func_2():
        e = -1

        def func_3():
            e = 10
            print(e)

        func_3()

    func_2()


func_1()