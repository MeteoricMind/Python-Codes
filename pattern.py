
# num = 5
# for i in range(num):
#     for j in range(i+1):
#         print(i,end="")
#     print(" ")

# r = 6
# a = range(r+1)
# print(a)

# for i in range(4):
#     for j in range(i+1,5):
#         print(j,end="")
#     print()

# num = 6
# for i in range(num):
#     for j in range(i):
#         print(i,end="")
#     print()

# 11111
# 2222
# 333
# 22
# 1

# for i in range(1,4):
#     for j in range(6-i):
#         print(i,end="")
#     print()
# for i in range(2,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print()
# ##----------------------------------------
# row= 5
# b = 0
# for i in range(row,0,-1):
#     b+=1
#     for j in range(row,1,i+1):
#         print(b,end="")
#     print()
###_____________________________________________

# This is the example of print simple reversed right angle pyramid pattern  
# rows = int(input("Enter the number of rows:"))  
# k = 2 * rows - 2  # It is used for number of spaces 
# print(k) 
# for i in range(0, rows):  
#     for j in range(0, k):  
#         print(end=" ")  
#     k = k - 2   # decrement k value after each iteration  
#     for j in range(0, i + 1):  
#         print("* ", end="")  # printing star  
#     print("") 

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() 

n = int(input("Enter the number of rows: "))  
m = (n) - 1
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ")  

# n = int(input("Enter a number of pattern: "))

# for i in range(n):
#     for j in range(n-i,0,-1):
#         print(" ",end="")
    
#     for x in range(n):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print(i,end="")
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(n,end="")
#     print()

# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print()

# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print(" * ",end="")
#     # for j in range(i):
#     #     print("*",end="")
#     print()

n = int(input("Enter the number of rows: "))  
#m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0,n-i):  
        print(end=" ")  
    #m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ") 

# rows = int(input("Enter the number of rows: "))  
  
# # It is used to print space  
# k = 2 * rows - 2  
# # Outer loop in reverse order  
# for i in range(rows, -1, -1):  
#     # Inner loop will print the number of space.  
#     for j in range(k, 0, -1):  
#         print(end=" ")  
#     k = k + 1  
#     # This inner loop will print the number o stars  
#     for j in range(0, i + 1):  
#         print("*", end=" ")  
#     print("")  


# a = 1
# num = int(input("Enter a number:"))
# for i in range(1,num+1):
#     for j in range(i):
#         print( a ,end=" ")
#         a = a+1

#     print()

n = int(input("Enter the number of rows: "))    
for i in range(0, n):  
    for j in range(0,n-i):  
        print(end=" ")   
    for j in range(0, i + 1):    
        print("* ", end="")  
    print(" ") 