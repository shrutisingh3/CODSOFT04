import random
user_input=int(input("Enter your choice :  Type 0 for Rock 1,1 for Paper,2 for Scissors:  "))
if user_input>=3 or user_input<0:
    print("You entered invalid number,You lose.")
else:
    c_choice = random.randint(0,2)
    print("Computer choose: ")
    print(c_choice)
    if c_choice == user_input:
        print("It's a draw")
    elif c_choice==0 and user_input==2:
        print("You Lose")
    elif c_choice==2 and user_input==0:
        print("You Win")
    elif c_choice>user_input:
        print("You Lose")
    elif user_input>c_choice:
        print("You Win")