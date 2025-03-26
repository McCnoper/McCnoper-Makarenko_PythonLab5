print("Task 1")
import random
num = random.randint(1,10)
x = 0
print("num is: "+str(num))
while x!=num:
    x = int(input())
    if x>num:
        print("Smaller")
    elif x<num:
        print("Bigger")
print("You guessed number")
print("-----------------------------------")
print("Task 2")
num = random.randint(1,50)
x = 0
print("num is: "+str(num))
while x!=num:
    x = int(input())
    if 3>=abs(x-num):
        print("Very near")
    elif 10>abs(x-num):
        print("Near")
    elif 10<abs(x-num):
        print("Far")
print("You guessed number")
print("-----------------------------------")
print("Task 3")
num = random.randint(1,10)
x = 0
print("num is: "+str(num))
att=3
while x!=num and att!=0:
    x = int(input())
    if x>num:
        print("Smaller")
    elif x<num:
        print("Bigger")
    att=att-1
if x==num: print("You guessed number")
else:
    print("Attempts are over")
    print("Number is "+str(num))
print("-----------------------------------")
print("Task 4")
num1 = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)
num4 = random.randint(1,9)
print("Pass code is: "+str(num1)+str(num2)+str(num3)+str(num4))
pss= False
att=5
print("Write only one digit")
while pss==False and att!=0:
    corr = 0
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    if x1==num1: corr += 1
    if x2==num2: corr += 1
    if x3==num3: corr += 1
    if x4==num4: corr += 1
    print("Number of correct numbers "+str(corr))
    if x1==num1 and x2==num2 and x3==num3 and x4==num4:
        pss=True
    else: att-=1
if pss==True:
    print("You guessed code")
else:
    print("Attempts are over")
    print("Number is "+str(num1,num2,num3,num4))
