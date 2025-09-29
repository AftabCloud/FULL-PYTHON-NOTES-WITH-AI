# # Assignment 1: Count Characters in a String python
# # Assignment 1: Count Characters in a String

# # Get a string from the user
# user_input = input("Enter a string: ")
# # Count all the characters (including spaces)
# count = len(user_input)
# # Show the result
# print("Number of characters (including spaces):", count)
# # Sample Input:
# # Hello World!

# # Expected Output:
# # Number of characters (including spaces): 12

# # Assignment 2: Extract a Substring
# # Get a string from the user
# user_input = input("Enter a string: ")
# # Get the start index number
# start = int(input("Enter the start index: "))
# # Get the end index number (not included)
# end = int(input("Enter the end index: "))
# # Get the substring from the user string
# substring = user_input[start:end]
# # Show the substring
# print("Extracted substring:", substring)
# # Sample Input:
# # PythonProgramming
# # Start: 6
# # End: 16

# # Expected Output:
# # Extracted substring: Programming

# # Assignment 3: Identify Palindromes
# # python
# # Assignment 3: Identify Palindromes
# # Get a word from the user
# word = input("Enter a word: ")
# # Check if the word is the same forwards and backwards
# if word == word[::-1]:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")
# # Sample Input:
# # level

# # Expected Output:
# # It is a palindrome.

# # Assignment 4: Replace All Occurrences of a Word python
# # Get a full sentence from the user
# sentence = input("Enter a sentence: ")
# # Get the word to change
# old_word = input("Enter the word to replace: ")
# # Get the new word
# new_word = input("Enter the new word: ")
# # Replace all old words with the new one
# result = sentence.replace(old_word, new_word)
# # Show the new sentence
# print("Updated sentence:", result)
# # Sample Input:
# # The cat jumps over the cat.
# # cat
# # dog

# # Expected Output:
# # Updated sentence: The dog jumps over the dog.

# # Assignment 5: Count Specific Word Occurrence  python
# # Get a paragraph from the user
# paragraph = input("Enter a paragraph: ")
# # Get the word to count
# word = input("Enter the word to count: ")
# # Split the paragraph into a list of words
# words_list = paragraph.split()
# # Count how many times the word appears
# count = words_list.count(word)
# # Show the count
# print(f"The word '{word}' appears {count} times.")
# # Sample Input:
# # Data science uses data and science methods. Data is everywhere.
# # Expected Output:
# # The word 'Data' appears 2 times.