	class Mobile:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
m1 = Mobile()
m1.set_color("Blue")
m1.set_cost(20000)
print(m1.show_color())
print(m1.show_cost())

class Phone:
    def make_call(self):
        print("I am making a call.")

    def play_game(self):
        print("I am playig a game.")

p1 = Phone()
p1.make_call()
p1.play_game()
#-------------------------------------------------------------                      
                    # Class and Instance Variables


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

#-------------------------------------------------------------
                    #Constructors in Python
class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()