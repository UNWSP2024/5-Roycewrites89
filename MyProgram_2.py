#Royce Daniel 2/20/2026 "math test"
print("You will be asked 10 simple math questions. Answer them as best you can.")
import random

def quiz():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    print("  ", num1)
    print("+ ", num2)
    print("------")
    useranswer = int(input("Your answer: "))
    realanswer = num1 + num2
    if useranswer == realanswer:
        print("Excellent! That is correct!")
    else:
        print("That's not quite right.")
        print("The correct answer is:", realanswer, "Try again. And do better next time")
for i in range(10):

 print(quiz())
