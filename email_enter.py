import re

def email_enter():

    email_input = input("Please enter your email.\n")

    pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-z]{3}')

    email_check = pattern.search(email_input)

    if email_check == None:
        print(f"\n|{email_input}| is not a valid email address. Please enter again.\n")
        email_enter()
    else:
        print(f"Email |{email_input}| has been entered into our system. Thank you.")

email_enter()


