'''
def add(a,b):
	""" hii my name is Aritra"""
    return a+b
    #print(c)
	

# print(add(3,5))
print(functions.__doc__)

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student('Practice','Geeks')

#------------------------------------------------------------------------------------------

                                #*args (Non-Keyword Arguments)
								#**kwargs (Keyword Arguments)

def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

###---------------------------------------------
def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

###  ---------------------------------------------
# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" % (key, value))

# myFun('hii' ,first='Geeks', mid='for', last='Geeks')

## USE OF ARGS AND KWARGS       ------------------------------
def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

#____________________________________________________________________________________________________________________________________
'''
# def simpleGeneratorFun():
#     yield 3            
#     yield 1            
#     yield 2            
   
# # Driver code to check above generator function
# for value in simpleGeneratorFun(): 
#     print(value)

'''
#_____________________________________________________________________________________________________________________________________

                        #LAMBDA FUNCTION

n = int(input("Enter a number:"))
x = lambda n: n+10
print(x(n))

minus = lambda x,y : x-y
print(minus(7,3))


#______________________________________________________________________________________________________________________________________

                            #Global and Local Variables in Python
						
a = 5
def fun():
	#global a
	a = 6
	print(a)
	s = "I love Geeksforgeeks"
	print(s,a)
a = 8
fun()
print(a)
a = 89
print(a)


# a = 15

# def change():
# 	a = a + 5
# 	print(a)

# change()


# Python program showing a use of
# global in nested function

def add():
	x = 15
	def change():
		global x
		x = 20
	print("Before making changing: ", x)
	print("Making change")
	change()
	print("After making change: ", x)

add()
print("value of x", x)
'''
##__________________________________________________________________________________________________________________________________

								# DECORATORS IN PYTHON
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)

def func(n):
	def func1():
		return "Endureka"
	def func2():
		return "Python"
	if n==1:
		return func1
	else:
		return func2

a = func(1)
b = func(2)
print(a())
print(b())



print("Hello world")
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    new_list = [[i,j,k] for i in range (x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
    print(new_list)


n = int(input())
    arr = map(int, input().split())
    #print(sorted(arr)[-2])
    
    list2 = list(set(arr))
 
# Sorting the  list
    list2.sort()
    print(list2[-2])