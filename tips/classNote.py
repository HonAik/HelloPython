#class and object

# #name a class:每个字连在一起然后每个words前面要大写： InfoName

# class CarInfo:
#     pass

# #create an object
# c1 = CarInfo() #no need new

# #manual add attribute to the object #not recommend because u did not use the class to ass attribute
# c1.colour = "Red"
# c1.brand = "Toyota"
# c1.name = "Car1"
# c1.price = 100000

# print(c1.brand)
# print(c1.__dict__) #__dict__ means use dictionary{} to store their attributes

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#recommend way: dynamic

class CarInfo:

    #static attribute:
    wheel = 4


    #in java, __init__ = constructor and self = this
    def __init__(self,colour,name,brand,price):
        self.colour = colour
        self.name = name
        self.brand = brand
        self.price = price
        self.wheel = 2

    def phonk(self):
        print(f"{self.name} is running")
    
    def driver(self,name,age):

        if age>=18:
            print(f"{name} is the driver and legal to drive because the driver is {age} years old")
        else:
            print(f"{name} is the driver and illegal to drive because the driver is {age} years old")
    
    def discount(self,discount):
        return self.price - discount
    
    def __str__(self): #可用于把object 变string
        return f"{self.name}, {self.brand} ,{self.colour}"
    
    def __lt__(self, other): #比较smaller
        return self.price < other.price
    
    def __eq__(self, other): #ifequalthen
        return self.name == other.name and self.brand == other.brand and self.colour == other.colour
    


        
car1 = CarInfo("Red","Car123","Toyota",1234567)
print(car1.__dict__)
car1.phonk()
car1.driver("Ray",18)
total_price = car1.discount(1000)
print(f"the total cost of this car is {total_price}")

# print(car1.wheel)#4
print(CarInfo.wheel)#4
#after put self.wheel=2 
print(car1.wheel)#2

car2 = CarInfo("Black","Car345","Vios",123467)
print(car2.__dict__)

#__x__method
print(car1)
print(car1 == car2) 
print(car1 < car2) 


