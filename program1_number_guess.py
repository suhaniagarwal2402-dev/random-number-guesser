import random
def newnumber():
    return (random.randint(1, 100))

def options():
    while True:
        print("\nMenu:")
        print("Press 1 to start/continue the game")
        print("Press 0 to exit the game")
        try:
            choice = int(input("Enter your choice: "))
            if choice==1:
                return True
            elif choice==0:
                print("Thank you for playing! Goodbye.")
                return False
            else:
                print("Invalid choice. Please enter 1 to start or 0 to exit.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")
    target_number=newnumber() 
    if not options():
        return
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
            target_number = newnumber()
            if options():
                target_number = newnumber()
            else:
                break  
main()                  
