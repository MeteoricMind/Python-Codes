# # class car:
# #     vehicle = 'Car'

# #     def setcolor(self,color):
# #         self.color = color

# #     def setmilage(self,milage):
# #         self.milage = milage

# #     def setleft(self,left):
# #         self.left = left
# #         print("Move left")

# # farari = car()
# # farari.setcolor('blue')
# # farari.setmilage(1000)

# # print(farari.setcolor())
# # print(farari.setmilage())


# class Dog:
 
#     # A simple class
#     # attribute
#     attr1 = "mammal"
#     attr2 = "dog"
 
#     # A sample method
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)
 
 
# Rodger = Dog()
# print(Rodger.attr1)
# Rodger.fun()


# ##########################################3
# class Person:
# 	def __init__(self, name):
# 		self.name = name

# 	def say_hi(self):
# 		print('Hello, my name is', self.name)


# p = Person('Nikhil')
# p.say_hi()
# ###################################

class Car:
	
    def __init__(self,make,model,color,mileage):
          self.make = make
          self.model = model
          self.color = color
          self.mileage = mileage

    def drive(self):
          print("I'm driving")
    def stop(self):
          print("This car is stop") 

car_1 = Car("chevy","cor","red","500")

print(car_1.make)
print(car_1.model)
print(car_1.color)
print(car_1.mileage)
Car.drive