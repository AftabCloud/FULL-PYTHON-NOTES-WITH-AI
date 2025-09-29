# USE CASES OF STRING & STRINGS MANIPULATION
# 1.CREATE A SIMPLE TEXT ANALYSIS PROGRAM
# WRITE A PYTHON PROGRAM THAT ANALYZES A PARAGRAPH OF TEXT BY:
# 1.COUNTING THE NUMBER OF WORDS.
# 2.COUNTING THE NUMBER OF SENTENCES.
# 3.REPLACING A SPECIFIC WORD WITH ANOTHER WORD PROVIDED BY THE USER.
paragraph = input("ENTER A PARAGRAPH OF TEXT: ")

#COUNT THE NUMBER OF WORDS
words = paragraph.split()
num_words = len(words)
print("NUMBER OF SENTENCES: ", num_words)

#COUNT THE NUMBER OF SENTENCES  (ASSUMING SENTENCES END WITH A PERIOD)
num_sentences = paragraph.split()
print("NUMBER OF SENTENCES:", num_sentences)


#REPLACE A SPECIFIC WORD 
old_word = input("ENTER THE WORD TO REPLACE: ")
new_word = input("ENTER THE NEW WORD: ")
updated_paragraph = paragraph.replace(old_word, new_word)
print("/n updated paragraph") 
updated_paragraph