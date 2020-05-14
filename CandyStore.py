class Customer:
    def __init__(self, firstname, lastname, money):
        self.firstname = firstname
        self.lastname = lastname
        self.money = money

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)


class CandyBar:
    def __init__(self, brandname, price):
        self.brandname = brandname
        self.price = price
        if self.brandname == "Twix":
            print("Ok, good choice! That will be 8$")
        if hasattr(cust_1.money) >= 8:
            print("Sold")
        else :
            print('You dont have enough money')



cust_1 = Customer('Austin', 'Bao', 20)
print(cust_1.fullname())

cust_bar_1 = CandyBar('Twix', 10)
print(cust_bar_1.brandname, cust_bar_1.price,'$')