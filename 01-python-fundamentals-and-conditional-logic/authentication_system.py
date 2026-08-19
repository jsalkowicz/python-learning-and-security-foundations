# Guided exercise: Authentication System
# Customized by adding a third input and an additional failure message.

username = "root"
password = "admin"
birthday = 123455

entered_username = input("Enter the username: ")
entered_password = input("Enter the password: ")
entered_birthday = int(input("Enter birthday: "))

if (
    entered_username == username
    and entered_password == password
    and entered_birthday == birthday
):
    print("Authentication successful")
else:
    print("Wrong username/password/birthday")
    print("Please try again later")
