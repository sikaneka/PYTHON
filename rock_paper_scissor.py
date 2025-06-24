import random
choice=['Rock','Paper','Scissor']

while True:
    com_choice=(random.choice(choice)).lower()
    print(f"Computer choice is: {com_choice}")
    user_choice=input("Enter your choice:\n1.Rock\n2.Paper\n3.Scissor\n").lower()
    if com_choice==user_choice:
        print("its a tie")
    elif (com_choice=='rock' and user_choice=='paper') or (com_choice=='paper' and user_choice=='scissor') or (com_choice=='scissor' and user_choice=='rock'):
        print("user wins")
    elif (com_choice=='rock' and user_choice=='scissor') or (com_choice=='paper' and user_choice=='rock') or (com_choice=='scissor' and user_choice=='paper'):
        print("computer wins")
    else:
        print("Your choice is invalid")
    n=input("Do you want to play again:(Y/N): ")
    if n.lower()=='n':
        print("Thanks for playing")
        break
    else:
        print("Enjoy your game")


