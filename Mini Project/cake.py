class Cake:
    def __init__(self, cake_no, cake_name, price, weight, quantity):  #  __init__ function call when obj of class is created
        self.cake_no = cake_no
        self.cake_name = cake_name
        self.price = price
        self.weight = weight
        self.quantity = quantity
        

    def __str__(self):  # represents class objects as a string
        return str(self.cake_no)+ "," +self.cake_name+ "," +str(self.price)+ "," +str(self.weight)+ "," +str(self.quantity)+"\n"

