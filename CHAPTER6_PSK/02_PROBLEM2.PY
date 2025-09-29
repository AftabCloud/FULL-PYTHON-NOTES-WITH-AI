# WRITE A PROGRAM TO FIND OUT WHETHER A STUDENT HAS PASSED OR FAILED
# IF IT REQUIRES A TOTAL OF 40% AND AT LEAST 30% IN EACH SUBJECT TO PASS
# ASSUME 3 SUBJECTS AND TAKES MARKS AS AN INPUT FROM THE USER
marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))

# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed:", total_percentage)

else:
    print("you failed,try next year:", total_percentage)