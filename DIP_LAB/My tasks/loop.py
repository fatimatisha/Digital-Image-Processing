password = None
attempts = []
while password != "myPassword1234":
    password = input("Enter the password:")
    attempts.append(password)
    if password != "myPassword1234":
        print("Your password is incorrect. You have already guessed:")
        for i in attempts:
            print(i)
    print("Correct password. Welcome.")
