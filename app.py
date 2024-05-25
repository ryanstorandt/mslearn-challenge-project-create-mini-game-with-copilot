#Create a rock paper scissors game
#Create a function that takes in a user choice and a computer choice
#The computer choice is randomly selected from a list of choices
#Compare the user choice and computer choice
#Determine the winner
#Return the result
#Create a main function that runs the game
#Prompt the user for their choice
#Call the function with the user choice and a random computer choice
#Print the result
#Allow the user to play again
#Create a loop that continues to run the game until the user decides to stop
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "User wins!"
    else:
        return "Computer wins!"

def print_ascii(choice):
    if choice == "rock":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif choice == "paper":
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif choice == "scissors":
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

def main():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(choices)
        print("Computer chose:")
        print_ascii(computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()