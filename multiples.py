
# # 1. first thing that came to mind solution: O(n) complexity
# total = 0
# for i in range(1, 1001):
#     total += i

# print(total)
    
# # 2. formula solution: computes in O(1) so is most efficient
# # the sum of n integers can be calculated using a formula:
# # sum = n * (n + 1) // 2

# n = 1000
# total = n * (n + 1) // 2
# print(total)

# # 3. sum() solution: internally optimised, so theoretically faster than for loop but still O(n)
# total = sum(range(1, 1001))
# print(total)

# # ESSAY WRITING
# # 1. TITLE Essay writing, first idea capitalisation:
# def capitalise_title(title:str) -> str:
#     title = title.strip()
#     if len(title) == 0:
#         return title
#     first_letter = title[0].upper()
#     rest_of_title = title[1:]
#     return first_letter + rest_of_title

# title = ' my hobbies '
# capitalised = capitalise_title(title)
# print(capitalised)

# # 2. TITLE using capitalize()
# def capitalise_title(title:str) -> str:
#     return title.strip().capitalize()

# title = ' my hobbies'
# capitalised = capitalise_title(title)
# print(capitalised)

# # 3. TITLE using title() - capitalises first letter of each word
# def capitalise_title(title:str) -> str:
#     return title.strip().title()

# title = ' my hobbies'
# capitalised = capitalise_title(title)
# print(capitalised)

# # 4. FULL STOP - first idea
# def check_sentence_ending(sentence:str) -> str:
#     if len(sentence) == 0:
#         return 'input valid sentence'
#     if sentence[-1] == '.':
#         return sentence
#     else:
#         sentence += '.'

#     return sentence

# sentence = 'hello.'
# correct_punctuation = check_sentence_ending(sentence)
# print(correct_punctuation)

# #  5. FULL STOP using endswith()
# def check_sentence_ending(sentence:str) -> str:
#     if not sentence:
#         return 'input valid sentence'
#     if not sentence.endswith('.'):
#         sentence += '.'
#     return sentence

# sentence = 'hello'
# correct_punctuation = check_sentence_ending(sentence)
# print(correct_punctuation)

# # 6. FULL STOP using regex
# import re

# def check_sentence_ending(sentence:str) -> str:
#     """
#     Ensures the sentence ends with a single period ('.').

#     - Removes trailing spaces and periods.
#     - Appends a single period at the end if it's missing.
#     """
#     # re.sub removes the matched characters [.\s] - fullstops and trailing whitespace
#     sentence = re.sub(r'[.\s]+$', '', sentence)  
#     # Add a single period at the end
#     return sentence + '.'

# sentence = 'hello...   '
# corrected_sentence = check_sentence_ending(sentence)
# print(corrected_sentence) 

# # 7. SPACING CLEANUP using regex
# import re

# def clean_up_spacing(sentence: str) -> str:
#     cleaned_sentence = re.sub(r'\s+', ' ', sentence)
#     return cleaned_sentence.strip()

# sentence = ' This   is a  sentence   with(out)  extra    spaces.   '
# cleaned = clean_up_spacing(sentence)
# print(cleaned)

# # 8. SYNONYMS - first solution that came to mind
# def replace_word_choice(sentence: str, old_word: str, new_word:str) -> str:
#     word_lst = list(sentence.split(" "))
#     for i in range(len(word_lst)):
#         if word_lst[i] == old_word:
#             word_lst[i] = new_word
#     new_sentence = " ".join(word_lst)
#     return new_sentence

# sentence = 'I bake good cakes.'
# old_word = 'good'
# new_word = 'amazing'

# new_sentence = replace_word_choice(sentence, old_word, new_word)
# print(new_sentence)

# # 9 SYNONYMS using str.replace() - downside, 
# #will replace substrings within words (e.g. goodbye -> amazingbye)

# def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
#     return sentence.replace(old_word, new_word)

# sentence = 'I bake good cakes.'
# old_word = 'good'
# new_word = 'amazing'

# new_sentence = replace_word_choice(sentence, old_word, new_word)
# print(new_sentence)

# 10 SYNONYMS using regex, keeps to word boundaries
# import re

# def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
#     #r - raw string literal ( python does not iterpret '\' as escape chars.)
#     #f - formatted string literal, allows to embed variables using {}
#     #\b - word boundary(not a space, just denotates where word begins/ends)

#     return re.sub(rf'\b{old_word}\b', new_word, sentence)

# sentence = 'I bake good cakes.'
# old_word = 'good'
# new_word = 'amazing'

# new_sentence = replace_word_choice(sentence, old_word, new_word)
# print(new_sentence)

