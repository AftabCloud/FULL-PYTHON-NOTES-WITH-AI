# #---------------- READING THE CONTENTS OF FILE---------------------
# # with open('sample.txt', 'r') as file:
# #     content = file.read()
# #     print('File content :\n',  content)


# # 🔹 1. Opening a File
# # Python uses the open() function.
# # file = open("filename.txt", "mode")
# # Common Modes:
# # •	"r" → Read MODE(default) – error if file not found
# # •	"w" → Write MODE– creates new file / overwrites existing (original content will be removed and what you written there.
# # •	"a" → Append  MODE– adds data to end of file(original data is there not remove anything just append what you gonna write
# # •	‘r+’ (read and write mode)
# # •	"x" → Create MODE – creates new file, error if file exists
# # •	"b" → Binary mode (e.g., images, videos)
# # •	"t" → Text mode (default)
# ________________________________________
# # 🔹 2. Reading from a File
# # Reading files: methods include: read(), readline(), and readlines.
# f = open("sample.txt", "r")
# print(f.read())        # read entire file
# print(f.read(10))      # read first 10 characters
# print(f.readline())    # read one line
# print(f.readlines())   # read all lines into a list
# f.close()
# # ________________________________________
# # 🔹 3. Writing to a File
# # Writing to files: use the write () or writelines() methods.
# f = open("sample.txt", "w")
# f.write("Hello, Python!\n")
# f.write("File handling is easy.")
# f.close()
# # # 👉 Note: "w" will overwrite existing file.
#  ________________________________________
#  🔹 4. Appending to a File
# f = open("sample.txt", "a")
# f.write("\nThis line is added later.") #
# f.close()
# # ________________________________________
# # 🔹 5. Using with (Best Practice)
# # No need to call close(), Python handles it automatically.
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
# # ___________________
# Handling File Exceptions in Python step by step.
# In real-world Data Engineering, files might:
# •	Not exist,
# •	Be locked by another process,
# •	Be corrupted,
# •	Have permission issues.
# That’s why we use exception handling (try-except) with file operations.
# 🔹 1. Basic Try–Except
# try:
#     with open("sample.txt", "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: The file does not exist.") 
#_____________________
# # 🔹 6. Working with Binary Files
# Reading an image
# with open("image.jpg", "rb") as f:
#     content = f.read()

# # Writing binary data
# with open("copy.jpg", "wb") as f:
#     f.write(content)
# # ________________________________________
# # 🔹 7. Checking if File Exists
# import os

# if os.path.exists("sample.txt"):
#     print("File exists")
# else:
#     print("File not found")
# # ________________________________________
# # 🔹 8. Deleting a File

# import os

# os.remove("sample.txt")   # delete file
# os.rmdir("foldername")    # delete empty folder

