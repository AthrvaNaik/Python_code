import re
email_cond="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter Email: ")
if re.search(email_cond,user_email):
    print("Email entered correctly")
else:
    print("Wrong Email")
