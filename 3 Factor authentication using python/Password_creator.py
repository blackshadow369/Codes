def password_maker():
    flag = 0
    while True:
        pass1 = input("Enter password :")
        pass2 = input("Confirm password :")
        if pass1==pass2 :
            print("PASSWORD CREATED ")
            return pass1
        else:
            print('PASSWORD NOT MATCHED. TRY AGAIN')
