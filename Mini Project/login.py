from cake import Cake
    
if(__name__=="__main__"):
    choice = 0
    while(choice != 3):
        print()
        print("---------------------------------------------------------------------")
        print("---------------------Welcome to Cake Shop!---------------------")
        print("---------------------------------------------------------------------")
    
        print("Choice 1: Admin Login","Choice 2: Customer Login", "Choice 3: Exit" "\n")

        choice = int(input("Enter your choice:"))
       
        if (choice == 1):
            password = input("Enter the password: ")
            if password=="Cake@123":
                print("Login Successfully")
            else:
                print("Login Failed")

        elif (choice == 2):
            pass

        elif (choice == 3):
            pass
        
    else:
            print("Invalid Choice!")