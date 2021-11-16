# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


# letter = input('Enter a letter in the alphabet (a-z or A-Z):').lower()
# if letter in 'a e i o u':
#   print(f'The letter {letter} is a vowel')
# elif letter in 'y':
#   print(f'the letter {letter} is sometimes a vowel')
# else:
#   print(f'The letter {letter} is a consonant')




  # exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.


phrase = ''
while phrase != 'quit':
  phrase = input('Please enter a word or phrase: ')
  print(f'The phrase you entered is {len(phrase.replace(" ", ""))} characters long')

