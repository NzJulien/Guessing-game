from random import randint
user_score = 0
computer_score = 0

while True:
    user = int(input("Enter a number between 1-10: "))
    computer = randint(1,10)
    if user == computer:
        user_score+=1
        break
    else:
        print("Try Again!")
        computer_score+=1
if computer_score > user_score:
    print(f"Computer wins with {computer_score} !")
elif computer_score < user_score:
    print(f"User wins with {user_score} !")
else:
    print("It's a Tie!")