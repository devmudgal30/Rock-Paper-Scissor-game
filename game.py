import random
choices = ("rock","paper","scissor")
computer = random.choice(choices)


you = input("choose rock/paper/scissor: ").lower()

print(f"you choose : {you}")
print(f"computer choose : {computer}")
if computer == you:
    print("Tie!")
elif computer!=you:
    if computer == "rock" and you == "paper":
        print("you wins")  
    elif computer == "rock" and you == "scissor":
        print("computer wins")  
    elif computer == "paper" and you == "scissor":
        print("you wins")  
    elif computer == "paper" and you == "rock":
        print("computer wins")  
    elif computer == "scissor" and you == "rock":
        print("you wins")  
    elif computer == "scissor" and you == "paper":
        print("you wins") 
else:
    print("something went wrong!")