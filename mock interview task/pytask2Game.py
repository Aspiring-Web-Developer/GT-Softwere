import random

# computer_points=0
# user_points=0

# for round in range(1,4):
#     print(f'round{round}')

#     Check=random.choice(['snake','gun','water'])
#     user=input("Enter any snake,gun,water:-")

#     if Check==user :
#         print("tie")
#         print("No Points")
#         print("computer choice",Check)
#         print("your choise",user)
        
#     elif (Check == "snake" and user== "water") or \
#          (Check == "water" and user== "gun") or \
#          (Check== "gun" and user== "snake"):
#         print("computer choice",Check)
#         print("your choise",user)
        
#         print("Computer wins this round!")
#         computer_points += 1

#     elif (user== "snake" and Check== "water") or \
#          (user== "water" and Check == "gun") or \
#          (user== "gun" and Check== "snake"):
#         print("computer choice",Check)
#         print("your choise",user)
#         print("You win this round!")
#         user_points += 1
#     else:
#         print("computer wins")
# print("end")

# print("your point",user_points)
# print("computer points",computer_points)

# if user_points==computer_points:
#     print("game Tie")
# elif user_points>computer_points:
#     print("User wins")
# elif computer_points>user_points:
#     print("computer wins")

#------------------------------------------------------------------------------------------------------->

#word guess

Fixword=["python", "game", "developer", "program"]

choosen_word=random.choice(Fixword)
print("Welcome To The Great Girikalan Show")

under=["_"]*len(choosen_word)

attempt=6

while attempt>0 and "_" in under:
    print("find word ","".join(under))
    user=input(" Enter the Guss letter:- ")
