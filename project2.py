max_attempts = 5
correct_username = "david"

for attempt in range(max_attempts):
  username = input("Enter your username: ")

  if(username == correct_username):
    print("Welcome to my platform")
    break
  else:
    print("Incorrect Username")
