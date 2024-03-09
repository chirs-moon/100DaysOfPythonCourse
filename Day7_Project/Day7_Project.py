import random
import Day7_Project_Art as art7
import Day7_Project_Words


# Start of the game
print("Welcome to the Hangman Game!")
print(art7.logo)

lives = 6

# Generating a random word
chosen_word = random.choice(Day7_Project_Words.word_list)

# Generating as many blanks as letters in word

word = []
guessed = []
for a in range(len(chosen_word)):
    word.append("_")

print(f"{' '.join(word)} {len(chosen_word)}")

# User guess

while "_" in word and not lives == 0:
    guess = input("Guess a letter: ").lower()

    for x in range(len(word)):
        letter = chosen_word[x]
        if letter == guess:
            word[x] = letter

    if guess not in word and guess not in guessed:
        lives -= 1
        print(art7.stages[lives])
    elif guess in guessed:
        print(f"You've already guessed {guess}")

    if guess not in guessed:
        guessed += guess

    print(f"{' '.join(word)}")
    print(f"Letter you have already gussed: {', '.join(guessed)}")

if "_" not in word:
    end_game = True
    print("You win.")

if lives == 0:
    end_game = True
    print(f"The phrase was: {chosen_word}")
    print("You lose.")
