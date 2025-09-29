a = int(input("Enter Your Age: "))

# IF STATEMENTS NO: 01
if(a%2 ==0):        # statement no 1 runs different different if statement
    print("a is even")
# END OF STATEMENT NO 1

# IF STATEMENTS NO: 02
if(a>=18):          # statement no2 runs different along with below whole program
    print("you are above the age of consent: ")
    print("Good for you")
elif(a<0):
    print("you're entering a invalid  negative age")

elif(a==0):
    print("you're entering an invalid 0 age")



else:
    print("You are below the age of consent: ")

# END OF STATEMENT NO 2
print("End of the program")
   