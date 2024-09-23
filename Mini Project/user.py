import os
import tabulate
from tabulate import tabulate
from cake import Cake
class User:
    # display cake detail
    def displayCakeDetails(self):
        if (os.path.exists("data.txt")):
            with open("data.txt", "r") as fp:
                info = fp.read()
                print(info)
        else:
            print("Cake doesn't exist")

    # search cake detail by id
    def searchCakeDetails(self, cake_no):
        with open("data.txt", 'r') as fp:
            data = fp.readlines()
        found = 0
        for line in data:
            info = line.split(",")
            if(info[0]==str(cake_no)):
                found = 1
                print("Cake is Available")
                print(line)
        if(found==0):
            print("Cake is not Available")

    # Add to cart
    def addCakeItem(self, i1):
        with open("cart.txt", 'a') as fp:
             #convert cake object to string
            fp.write(str(i1))
    
    #Bill Generation
    def byeCake(self):
        if (os.path.exists("cart.txt")):
            #read & write
            with open("cart.txt", 'r+') as fp:
                total = 0
                for line in fp:
                    # store all the prices in 'total'
                    e_record = line.split(',')
                    total =  total+int(e_record[2]) * int(e_record[4])
                    fp.truncate(0)
            print('\nThanks for Puchasing Cake with us :)')
            print('Your total bill amount is ', total, '/-')


  