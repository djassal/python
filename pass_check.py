def pass_check(p):
    if int(len(p)) < 5:
        print("Length of password should not be less than 5.")
    elif int(len(p)) > 12:
        print("Length of password should not be greater than 12.")
    elif not "@" in p or "*" in p or "$" in p:
        print("Atleast one symbol (@ or * or $ ) should exist in the password.")
    elif p.upper() == p:
        print("Whole password cannot be uppercase.")
    else:
        print("Password Set Successfully!!")
    return p

password = input("Please enter your password(Max words 5-12, atleast one @,$,* and not in full uppercase): ")
pass_check(password)
