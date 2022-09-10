a = [1, 2, 3]
try: 
    #print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
  
except:
    print ("An error occurred")

#-----------------------------------------------------------

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)

# note that braces () are necessary here for multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")
#----------------------------------------------------------------
# Try with Else Clause
# In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
AbyB(6.0, 3.0)
#-------------------------------------------------------------