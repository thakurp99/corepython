import random

def game(com,you):
    if com == you:
        return None
    elif com == "s":
        if you == "w":
            return False
        elif com == "g":
            return True
    elif com == "w":
        if you == "g":
            return False
        elif com == "s":
            return True
    elif com == "g":
        if you == "s":
            return False
        elif com == "w":
            return True

print("Computer Turn : Press:- S-W-G :")
randNo = random.randint(1,3)
if randNo == 1:
    com = "s"
elif randNo == 2:
    com = "w"
elif randNo == 3:
    com = "g"

you = input("Your Turn : Press:- s,w,g :")
a = game(com,you)

print(f"Computer Chose {com}")
print(f"You Chose {you}")

if a == None:
    print("The game is tie")

elif a:
    print("You Win...")

elif a:
    print("You Lose")



