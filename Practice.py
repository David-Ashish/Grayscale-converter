print("Good afternoon!!!")

def foo():
    p = input("enter the password: ")
    return p

user_pass = foo()
print(user_pass)
password = len(user_pass)

if len(user_pass) >= 8:
    print(f"The password is true")
else:
    print(f"The password is false")
password = len(user_pass)
print(password)









