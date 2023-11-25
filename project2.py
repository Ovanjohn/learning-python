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