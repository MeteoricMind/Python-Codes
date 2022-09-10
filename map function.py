number = ["3","34","88"]

number = list(map(int,number))

# for i in range (len(number)):
#     number[i]= int(number[i])

number[2]= number[2]+4
print(number[2])

num = [2,7,5,88,9]
def sq(a):
    return a*a

num = list(map(sq,num))
print(num)
num = map(lambda a: a*a,num)
print(list(num))
print(num)

#--------------------------FILTER FUNCTION-----------------

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num > 5

gr_than_5 = filter(is_greater_5, list_1)
print(list(gr_than_5))