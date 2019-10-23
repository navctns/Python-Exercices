#login system
usr_name_orig='bridge'
pass_word_orig='river'

usr_name=input("Enter user name:")
pass_word=input("Password:")

"""if usr_name ==usr_name_orig:
    if pass_word==pass_word_orig:
        print("Login successful")
    else:
        print("Password is incorrect:")
else:
    print("Invalid credentials")
"""
if (usr_name==usr_name_orig) & (pass_word==pass_word_orig):
    print("Login successful")
else:
    print("Invalid credentials")
