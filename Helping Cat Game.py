print('''
*******************************************************************************
        .__....._             _.....__,
            .": o :':         ;': o :".
            `. `-' .'.       .'. `-' .'
              `---'             `---'

    _...----...      ...   ...      ...----..._
 .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
'.-'   _.--"""'       `-._.-'       '"""--._   `-.`
'  .-"'                  :                  `"-.  `
  '   `.              _.'"'._              .'   `
        `.       ,.-'"       "'-.,       .'
          `.                           .'
            `-._                   _.-'
                `"'--...___...--'"`
*******************************************************************************
''')
import time


# Function to handle the game logic
def play_game():
    print("Welcome to Help the Cat .")
    print("Your mission is to find the Cat before the Dog comes,you have 50s to help her!!!.")

    choice1 = input('You\'re at a crossroad, where do you want to go? '
                    'Type "left" or "right".\n').lower()

    if choice1 == "left":
        choice2 = input('You\'ve come to a lake. '
                        'There is an island in the middle of the lake. '
                        'Type "wait" to wait for a boat. '
                        'Type "swim" to swim across.\n').lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. "
                            "There is a house with 3 doors. One red, "
                            "one yellow and one blue. "
                            "Which color do you choose?\n").lower()
            if choice3 == "red":
                print("It's a room full of fire. Game Over")
            elif choice3 == "yellow":
                 print("You found the Cat.")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You got attacked by an angry trout. Game Over.")

    else:
        print("You fell into a hole. Game Over.")


# Start the timer
start_time = time.time()

# Call the function to start the game
play_game()

# Stop the timer after the game ends
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Check if the game took longer than 50 seconds
if elapsed_time > 50:
    print("Time's up! Game Over.")
else:
    print(f"Time taken: {elapsed_time:.4f} seconds")
