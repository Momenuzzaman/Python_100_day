import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Pssst, The solution is {chosen_word}")

display = []
for _ in range(len(chosen_word)):
    display.append("-")
print(display)

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
