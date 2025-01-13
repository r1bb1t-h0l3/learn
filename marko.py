number_of_words, number_of_letters = map(int, input().strip(). split(" "))

print(number_of_words, number_of_letters) 

words = {}
for i in range(number_of_words):
    word = input().strip()
    first_letter = word[0]
    if first_letter not in words:
        words[first_letter] = []

    words[first_letter].append(word)

for key in words:
    words[key] = sorted(words[key])

letters = []
for i in range(number_of_letters):
    letter = input().strip()
    letters.append(letter)

# create dictinary to keep track of number of times word was used
words_counter = {key: 0 for key in words}

for letter in letters:
    if letter in words:
        index = words_counter[letter]
        print(words[letter][index])
        words_counter[letter] = (index + 1) % len(words[letter])