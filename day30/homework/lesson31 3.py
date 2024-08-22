def check_password():
    password="Gelabarkalaia123"
    guess=""

    while guess != password :
        guess = input("enter your password:")

        print("password is correct")

check_password()