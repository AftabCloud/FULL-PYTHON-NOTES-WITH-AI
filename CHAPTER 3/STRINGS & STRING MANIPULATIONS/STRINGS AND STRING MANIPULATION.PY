#  A string is a sequence of characters (letters, numbers, symbols, spaces)
# enclosed in single quotes ' ', double quotes " ",
#  or triple quotes ''' ''' or """ """.
name = "ZAIN" 
       #0123 or -4-3-2-1
# name = 'ZAIN'
# name = '''ZAIN''' 
# we can write the strings in single or triple 
# strings are IMMUTABLE
nameshort = name[0:2] # start from 0 all the way till2 (excluding2)
print(nameshort)
charecter1 = name[3]
print(charecter1)
name = "Zain"
greeting = 'Hello World'
number_string = "12345"
# String = Text data in Python
#📘 String Manipulation in Python
#String manipulation means performing operations on strings 
# (changing, joining, slicing, searching, etc.).

# Common String Operations
#1. Concatenation (Joining Strings)
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World
#2. Repetition
word = "Hi "
print(word * 3)   # Hi Hi Hi

#INDEXING(ACCESS CHARECTERS)
TEXT = "PYTHON" 
print(TEXT[0])
print(TEXT[-1])
print(TEXT[-4])
print(TEXT[::2]) 

# SLICING (GET A PART OF STRING)
TEXT = "PYTHON"
print(TEXT[0:5])
print(TEXT[-3:])
print(TEXT[:4])
print(TEXT[0:-2])

#CHANGING CASES
MSG = "hello world"
print(MSG.upper())
print(MSG.lower())
print(MSG.title())

#6. Finding & Replacing(REPLACING OCCURRENCES OF A SUBSTRING)
text = "I love Python"
print(text.find("Python"))        # 7
print(text.replace("Python", "Java"))   # I love Java

#checking content
name = "Zain"
print(name.isalpha())   # True (all letters)
print("123".isdigit())  # True (all digits)
print(" ".isspace())    # True (only spaces)


NAME = "zain" 
print(len(NAME))
print(NAME.endswith("in")) #its a boolean gives true or false
print(NAME.startswith("za"))
print(NAME.capitalize())

#ESCAPE SEQUENCE
a = "zain is a good boy\n But raghees is a \tbad \"boy\"" 

print(a)
# \n is used for new line
# \t is used like a tab space
# \"boy\" is used for double coat

#COMMON STRING METHODS
#PYTHON PROVIDES SEVERAL BUILT-IN-METHODS FOR STRING MANIPULATION
MSG = "  hello, world"
print(MSG.upper()) #CONVERTS THE STRING TO UPPERCASE
print(MSG.lower()) #CONVERTS THE STRING TO LOWERCASE
print(MSG.title()) 
print(MSG.split (", ")) #SPLITS THE STRING INTO A LIST OF SUBSTRINGS.
print(MSG.strip()) #REMOVES LEADING AND TRAILING WHITESPACES
print(" ".join(["python", "is", "fun"])) #JOINS ELEMENTS OF AN ITERABLE INTO A SINGLE STRING.