max_attempts = 5
correct_username = "david"

for attempt in range(max_attempts):
  username = input("Enter your username: ")

  if(username == correct_username):
    print("Welcome to my platform")
    break
  else:
    print("Incorrect Username")

#Creating a user login system using While Loop
Max_attempts = 3
correct_username = "admin"
correct_password = "12345"
attempts = 1
username = input("Enter your username")
password = input("Enter your password")
while attempts < Max_attempts:
  if(username == correct_username and password == correct_password):
   break
  else:
      print("incorrect username or password")
      username = input("Enter your username")
      password = input("Enter your password")
      attempts = attempts + 1
      print(f"your number of attempts is { attempts}")


      #Creating a user login system using If Loop
Max_attempts = 3
correct_username = "admin"
correct_password = "12345"
for attempt in range( Max_attempts):
  username = input("Enter your usrename:")
  password = input("Enter your password:")
  if( username == correct_username and password == correct_password):
    print("login successful")
    breakEnter your usrename:admin

  else:
      print("incorrect username or password")#Creating a Result Application
correct_username = "uche"
correct_password = "ovanjohn"
username = input("Enter your username")
password = input("Enter your password")

if(username == correct_username and password == correct_password):
  print(f"welcome to our grading app {username}")
  no_total_scores = int(input("How many score do you want to input"))
  masterList = []
  start = 0
  while(start < no_total_scores):

   score = int(input("Enter your score"))
   if(score >= 70 and score <= 100):
      masterList.append("A")
   elif(score >= 60 and score <= 69):
      masterList.append("B")
   elif(score >= 50 and score <= 59):
      masterList.append("C")
   else:
      masterList.append("Fail")

            #increment
   start = start + 1
else:
     print("Your username or password is worng")
print(masterList)

#Creating a Result App using for loop
correct_username = "uche"
correct_password = "chid"

#Request username and password
username = input("Enter your username:")
password = input("Enter your password:")
if(username == correct_username and password == correct_password):
  print(f"Welcome to our App {username}")
  no_of_score = int(input("Enter the number of score you want to input"))
  masterList = []
  for i in range( no_of_score):
    score = int(input("Enter your score"))
    if(score >= 70 and score <= 100):
     masterList.append("A")
    elif(score >= 60 and score <= 69):
      masterList.append("B")
    elif( score >= 50 and score <= 50):
      masterList.append("C")
    else:
      masterList.append("Fail")
print(masterList)


#Greeting
def morningGreeting():
 print("Good morning to you")


morningGreeting()


def dayGreetingAndTime( greetings, time):
  print(f"Good Morning to you {greetings}, the time is {time} 9am")
greetings = input("Enter your greeting?")
time = input("Enter the time")

dayGreetingAndTime(greetings, time)


# 1. create a guessing where the user inputs a number and the program tells if the number is correct, too low or too high
import random
n = random.randrange(1, 10)
guess = int(input("Enter any number:"))
while n!= guess:
    if guess < n:
     print("Too low")
     guess = int(input("Enter number:"))
    elif guess > n:
      print("Too high")
      guess = int(input("Enter number:"))
    else:
      break
print("Correct")



#creating loop that print only odd number
number = int(input("Enter a number"))
for i in range(1, numbers +1):
 if(i % 2 ==1):
  print(i)

#creating loo that print only prime numbers
for num in range(1, 20):
  for i in range(2, num):
    if num % i == 0:
      break
    else:
        print(num)
        break


        #loo to create square of numbers
numbers =[4, 2, 6, 7, 8]
square = 0
for value in numbers:
  square = value **2
  squares = square
  print("The list of squares", square)


# A Voting Apllication Using Python
firstname = input("Enter your first name")
lastname = input("Enter your last name")
fullname = firstname +""+ lastname
print(f" welcome to our voting application {fullname}")
age = input("Enter your age ")
eligibleAge = 18
age = int(age)
if(age >= eligibleAge):
  print(f" you are eligible to vote {fullname}")
else:
  print("you are not eligible to vote")



a = 5
b = 7
c = a + b
print(c)
