def name(string):
    print(f"my name is {string}.")

def add(num1,num2):
    return num1+num2

print("And the name is ", __name__)
if __name__ == '__main__':
    name("Harry")
    o = add(3,7)
    print(o)