print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')
else:
    print("Incorrect!")

