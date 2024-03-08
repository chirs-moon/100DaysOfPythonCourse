print('''
       _~
    _~ )_)_~
    )_))_))_)
    _!__!__!_
    \\______t/
  ~~~~~~~~~~~~~
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
choice = input().lower()

if choice == "left":
    print("You came to a lake. There is an island in the middle of the lake. "
          "Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    choice = input().lower()
    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. "
              "One red, one yellow and one blue. Which color do you choose?")
        choice = input().lower()
        if choice == "blue":
            print("You enter a room of beats. Game Over!")
        elif choice == "red":
            print("You fall into a fire. Game Over!")
        elif choice == "yellow":
            print("Congratulations, you found the treasure! You Win!")
        else:
            print("Game Over!")
    else:
        print("You were attacked by a trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")

