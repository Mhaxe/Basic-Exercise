import random
#word_list
word_list = [
    'github', 'dictionary', "mathematics", 'coding', 'soccer', 'appreciation'
]

lives = 9
heart_symbol = u'\u2764'
word = random.choice(word_list)
guessed_word_correctly = False

index = 0
clue = []
for letter in word:
    clue.insert(index, '?')
    index = index + 1


def update_clue(guessed_letter, clue, word):
    index = 0
    while index < len(word):
        if guessed_letter == word[index]:
            clue[index] = guessed_letter
        index = index + 1


while lives > 0:
    print(lives * heart_symbol)
    print(clue)

    guess = input("please enter a letter or the whole word:  ")
    if len(guess) == 1 and guess.lower() in word:
        update_clue(guess.lower(), clue, word)
    elif guess == word:
        guessed_word_correctly = True
    else:
        print("Incorrect guess!")
        lives = lives - 1

    if '?' not in clue or guessed_word_correctly:
        print(f"You won! The secret word is {word}")
        break
    elif lives == 0:
        print(f"You lost! The secret word is {word}")
        break
