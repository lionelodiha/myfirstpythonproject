print("welcome to the quiz game! ")
playing = input("Do you want to play yes/no? ")

if playing != "yes":
    quit()

print("Okay! Let's pray :) ")
score = 0

answer = input("Who is the president of Nigeria? ")
if answer.lower() == "jagaban":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full meaning of CBN? ")
if answer.lower() == "central bank of nigeria":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full meaning of NAFDAC? ")
if answer.lower() == "national agency for food drug administration and control":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does a GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does a CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full meaning of RAM? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " answers correct")
print("you got " + str((score/5)* 100) + "% on the quiz")