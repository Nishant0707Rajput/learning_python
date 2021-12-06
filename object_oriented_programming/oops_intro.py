# a = 4
# b = 12
# print(a + b)
# print(a.__add__(b))           ------> IN python type is also a class.
class Kettle(object):

    power_source = "electricity"        #---------> class atrribute

    def __init__(self, make, price):
        self.make = make                #----------->data atrribute
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)    # -----------> an instance
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12
print(kenwood.price)
hamilton = Kettle("Hamilton", 78)
print(hamilton.make)
print(hamilton.price)

print(f"Models: {kenwood.make} = {kenwood.price} and {hamilton.make} = {hamilton.price}")

print("Models: {0.make} = {0.price} and {1.make} = {1.price}".format(kenwood, hamilton))
"""
Class : template for creating objects. All objects created from a class will have same characteristics.
Object: An instance of a class.
Instantiate: Create an instance of a Class.
Method : A function defined in a class.
Atrribute : a variable bound to an instance of a class.
"""
print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

print(hamilton.on)
Kettle.switch_on(hamilton)          # same thing alternate method
print(hamilton.on)

print("-"*80)
kenwood.power = 2
print(kenwood.power)
# print(hamilton.power)        ------>error because power var only defined in kenwood instance
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("Switching to atomic power")
Kettle.power_source = "atomic"

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("-"*80)

hamilton.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)           #----->new entry in hamilton dict
                                   #Concept of global variable
