login_attempts = 5
actual_password = "hello"

while login_attempts > 0:
    password = input("Enter Password: ")
    if (password != actual_password):
        print("Incorrect attempt")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
        if (login_attempts == 0):
            print("Account locked")
    else:
        print("Login Successful")
        break


