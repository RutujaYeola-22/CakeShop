import os
import tabulate
from texttable import Texttable
from cake import Cake

class Admin:
    # add cake detail
    def addCakeDetails(self, c1):
        with open("data.txt", 'a') as fp:
             #convert cake object to string
            fp.write(str(c1))

    # display cake detail
    def displayCakeDetails(self):
        if (os.path.exists("data.txt")): #check whether the specified path exists or not
            with open("data.txt", "r") as fp:
                info = fp.read()
                t = Texttable()
                t.add_rows([['Cake_Id', 'Cake_Name', 'Price', 'Weight', 'Quantity']])
                print(t.draw())
                #print(t.add_rows(info))
                print(info)
                
        else:
            print("Cake doesn't exist")

    # search cake detail by id
    def searchCakeDetails(self, cake_no):
        with open("data.txt", 'r') as fp:
            data = fp.readlines()
        found = 0
        for line in data:
            info = line.split(",")  #split() method splits a string into a list
            if(info[0]==str(cake_no)):
                found = 1
                print("Cake is Available")
                print(line)
        if(found==0):
            print("Cake is not Available")

    # delete cake detail by cake_no
    def deleteByCakeNo(self, cake_no):
        with open("data.txt", 'r') as fp:
            allCakeDetail = []
            isfound = False
            for line in fp:
                try:
                    #check if cake_no available
                    line.index(str(cake_no),0,3)
                except:
                    #not present add data to container
                    allCakeDetail.append(line)
                else:
                    #cake_no available 
                    isfound = True
            if (isfound == True):
                 #if cake_no available
                with open("data.txt", 'w') as fp:
                    for d in allCakeDetail:
                        fp.write(d)
            else:
                print("Cake not Available")

    # delete cake detail by name
    def deleteByCakeName(self, cake_name):
        if(os.path.exists("data.txt")):
            with open("data.txt", 'r') as fp:
                allCakeDetail = []
                isfound = False
                for line in fp:
                    try:
                        line.index(cake_name)
                    except:
                        allCakeDetail.append(line)
                    else:
                        isfound = True
                if (isfound == True):
                    with open("data.txt", 'w') as fp:
                        for d in allCakeDetail:
                            fp.write(d)
                else:
                    print("Cake not available: ")

    # Update cake detail 
    def updateByCakeNo(self, cake_no):
        if (os.path.exists("data.txt")):
            with open("data.txt", 'r') as fp:
                allCakeDetail = []
                isfound = False
                for line in fp:
                    try:
                        line.index(str(cake_no),0,3)
                    except:
                        allCakeDetail.append(line)
                    else:
                        #split() method splits a string into a list
                        e_record = line.split(',')
                        # name Update
                        ans = input("Do you want to change cake name: (yes/no): ")
                        if (ans.lower() == 'yes'):
                            new_name = input("Enter updated name: ")
                            e_record[1] = new_name
                        #price update 
                        ans = input("Do you want to change cake price:(yes/no): ")
                        if(ans.lower() == 'yes'):
                            new_price= int(input("Enter updated cake price: "))
                            e_record[2] = str(new_price)
                        # join elements of the sequence separated by a string separator
                        s = ','.join(e_record)
                        allCakeDetail.append(s)
                        isfound = True

            if(isfound == True):
                with open("data.txt", 'w') as fp:
                    for e in allCakeDetail:
                        fp.write(e)
            else:
                print("Cake not available")