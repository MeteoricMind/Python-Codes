##  ENUMERATE FUNCTION  ##
#:  enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.
l1 = ['The', 'Big', 'Bang', 'Theory']

for index , item in enumerate(l1):
    #if index % 2 == 0:
        print(f"{index+1} jarvis please buy {item}") 
#-------------------------------------------------------------------------------------

##   ZIP()  ##
#Way 2: Using zip(): zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially. The loop exists only till the smaller container ends.

questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

for q,a in zip(questions,answers):
    print("Whats your {0}?\n I am {1}.".format(q,a))

#---------------------------------------------------------------------------------------

##  ITEM()   ##
#Way 3: Using item(): items() is used to loop through the dictionary printing the dictionary key-value pair sequentially which is used before Python 3 version.
king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
        'Modi': 'The Changer'}
 
# using items to print the dictionary key-value pair
for key, value in king.items():
    print(key, value)
print(king)

#----------------------------------------------------------------------------------------
##   SORTED()  AND SET()   ###
#Way 5: Using sorted():  sorted() is used to print the container is sorted order. It doesn’t sort the container but just prints the container in sorted order for 1 instance. The use of set() can be combined to remove duplicate occurrences.

lis = [1, 3, 5, 6, 2, 1, 3]
print(sorted(lis))
print(sorted(set(lis)))

# using sorted() to print the list in sorted order
print("The list in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")
 
print("\r")

print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
    print(i, end=" ")

#-----------------------------------------------------------------------------------------

##   REVERSED()   ##
#Using reversed(): reversed() is used to print the values of the container in the reversed order. 

lis = [1, 3, 5, 6, 2, 1, 3]
print("\nThe list in reversed order is : ")
for i in reversed(lis):
    print(i,end="")
