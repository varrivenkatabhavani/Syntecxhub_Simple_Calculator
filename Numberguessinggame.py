import random
best_score = None
while True:
    print("\n===== NUMBER GUESSING GAME =====")
    print("Select Difficulty Level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        max_number = 50
    elif choice == '2':
        max_number = 100
    elif choice == '3':
        max_number = 200
    elif choice == '4':
        print("Game Closed.")
        break
    else:
        print("Invalid Choice!")
        continue
    secret_number = random.randint(1, max_number)
    attempts = 0
    print(f"\nI have selected a number between 1 and {max_number}.")
    print("Try to guess it!")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too Low! Try Again.")
            elif guess > secret_number:
                print("Too High! Try Again.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("New Best Score:", best_score)
                else:
                    print("Best Score:", best_score)
                break
        except ValueError:
            print("Please enter a valid number!")
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != 'yes':
        print("Thanks for Playing!")
        break