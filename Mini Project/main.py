from cake import Cake
import tabulate
from tabulate import tabulate
from admin import Admin
from user import User

# entry point allows our program to be executable by itself
if(__name__=="__main__"):
    ch = 0
    while (ch!=3):
        print("\n1. Admin \n2. User \n3. Exit")
        ch = int(input("Enter your choice: "))

        # Admin Part
        if (ch == 1):
            obj = Admin()
            password = input("Enter the password: ")
            if password=="Admin":
                print("Login Successfully")
            else:
                print("Login Failed")
                break

            choice = 0
            while(choice!=7):
                print('\n1. Add\n2. Display\n3. Search\n4. Delete\n5. Delete by name\n6. Update\n7. Exit')
                choice = int(input("Enter choice:"))

                if (choice == 1):
                    cake_no = int(input("Enter Cake_No: "))
                    cake_name = input("Enter Cake Name: ")
                    price = int(input("Enter Cake Price: "))
                    weight = input("Enter Cake Weight: ")
                    quantity = input("Enter Cake Quantity: ")
                    c1 = Cake(cake_no, cake_name, price, weight, quantity)
                    obj.addCakeDetails(c1)
            
                elif (choice == 2):
                    obj.displayCakeDetails()

                elif (choice == 3):
                    cake_no = int(input("Enter Cake_No: "))
                    obj.searchCakeDetails(cake_no)
                
                elif (choice == 4):
                    cake_no = int(input("Enter Cake_No: "))
                    obj.deleteByCakeNo(cake_no)

                elif (choice == 5):
                    cake_name= input("Enter Cake Name: ")
                    obj.deleteByCakeName(cake_name)
                
                elif (choice == 6):
                    cake_no = int(input("Enter cake_no: "))
                    obj.updateByCakeNo(cake_no)
                else:
                    print("Invalid Choice")
                    break
        
        # User Part
        elif(ch == 2):
            obj = User()
            password = input("Enter the password: ")
            if password=="User":
                print("Login Successfully")
            else:
                print("Login Failed")
                break
            choice = 0
            while(choice!=5):
                print('\n1. Display\n2. Search\n3. Add to Cart\n4. Total Bill\n5. Exit')
                choice = int(input("Enter choice:"))

                if (choice == 1):
                    obj.displayCakeDetails()

                elif (choice == 2):
                    cake_no = int(input("Enter Cake_No: "))
                    obj.searchCakeDetails(cake_no)

                elif (choice == 3):
                    d = input("Do you want to add to the cart (yes/no):")
                    if(d == 'yes'):
                        cake_no = int(input("Enter Cake_No: "))
                        cake_name = input("Enter Cake Name: ")
                        price = int(input("Enter Cake Price: "))
                        weight = input("Enter Cake Weight: ")
                        quantity = int(input("Enter Cake Quantity: "))
                        i1 = Cake(cake_no, cake_name, price, weight, quantity)
                        obj.addCakeItem(i1)

                elif (choice == 4):
                    obj.byeCake()

        else:
            print("Invalid Choice")
            break


