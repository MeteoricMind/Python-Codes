import random

a = input("Enter your name: ")
A = a.capitalize()
b = "Aritra"
B = b.capitalize()
c= print(f"So {A} my self {B}.Lets play rock paper sceisor.")

print("INSTRUCTION")

print("(a)Who ever complet first 5 point is the winner.")
print("(b) 0 for stone")
print("(c) 2 for seisor")
print("(d) 5 for paper")

print("SO lets start.")
GAME=[0,2,5]


ka = 0
hum=0

while ka<=5 or hum<=5:
          you=int(input("stone paper seisor: "))
          comp= random.choice(GAME)
          if you==comp:
                    print("Opps! both are same.")
          elif you==0:
                    if comp==5:
                              print(f"{B} goes with paper and you stone. So {B} won.")
                              ka = ka+1
                              if ka==5:
                                        print(f"{B} is the winer.")
                                        break
                              
                              print(f"so {B} score is {ka}. ")
                    else:
                              print(f"{B} goes with sceisor and you stone. So you won.")
                              hum = hum+1
                              if hum==5:
                                        print("Congrats, you are the winner.")
                                        break
                              
                              print(f"so your score is {hum}. ")
          elif you==2:
                    if comp==5:
                              print(f"{B} goes with paper and you sceisor. So you won.")
                              hum = hum+1
                              if hum==5:
                                        print("Congrats, you are the winner.")
                                        break
                              
                              print(f"so your score is {hum}. ")
                    else:
                              print(f"{B} goes with stone and you sceisor. So {B} won.")
                              ka = ka+1
                              if ka==5:
                                        print(f"{B} is the winer.")
                                        break
                             
                              print(f"so {B} score is {ka}. ")
          elif you==5:
                    if comp==2:
                              print(f"{B} goes with sceisor and you paper. So {B} won.")
                              ka = ka+1
                              if ka==5:
                                        print(f"{B} is the winer.")
                                        break
                              
                              print(f"so {B} score is {ka}. ")
                    else:
                              print(f"{B} goes with stone and you paper. So you won.")
                              hum = hum+1
                              if hum==5:
                                        print("Congrats, you are the winner.")
                                        break
                    
                              print(f"so your score is {hum}. ")
          
          else:
                    print("Please check your input.")