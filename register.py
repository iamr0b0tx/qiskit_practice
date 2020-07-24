from account import Account

def clean_name(name):
    return name.capitalize()

def make_lower(text):
    return text.lower()

def clean_account_type(account_type):
    return make_lower(account_type)

def clean_email(email):
    return make_lower(email)

def validate_name(name):
    for c in name:
        if c.isnumeric():
            return False
    return True

def validate_phone_number(phone_number):
    if len(phone_number) != 11:
        return False

    if not phone_number.isnumeric():
        return False

    return True

def validate_email(email):
    email_length = len(email)

    # the email length is not less than five
    if email_length < 5:
        return False

    # the @ symbol exists in the email only once
    if email.count("@") != 1:
        return False

    # the @ symbol is not in the beginning, not next to '.' and not after '.' and not at the end of the email
    if email.index("@") in [0, email.index(".")-1, email.index(".")+1, email_length-1]:
        return False

    # the . symbol should exist in the email only once
    if email.count(".") != 1:
        return False

    # the . symbol is not in the beginning, not next to '@' and not after '@' and not at the end of the email
    if email.index(".") in [0, email.index("@")-1, email.index("@")+1, email_length-1]:
        return False

    return True

def validate_account_type(account_type):
    if account_type not in ["savings", "current", "credit"]:
        return False
    return True

def get_input(prompt, clean_function, validate_function):
    ''' gets input from user with a prompt, clean the input and validate the input before return '''

    # initial boolean
    status = False

    # while the input is not valid
    while status is False:
        value = input(prompt)

        if make_lower(value.strip()) == 'q':
            exit()

        # collect input
        if clean_function is not None:
            value = clean_function(value)

        # get the validation status
        status = validate_function(value)

    # return a cleaned and validated input
    return value

def form_info():
    print("Fill the form accordingly. Type 'q' to quit the program.")

def register():
    # display help message for form
    form_info()
    
    # request information
    first_name = get_input("What is your First name?: ", clean_name, validate_name)
    last_name = get_input("What is your Last name?: ", clean_name, validate_name)
    email = get_input("What is your Email Address?: ", clean_email, validate_email)
    phone_number = get_input("What is your Phone number?: ", None, validate_phone_number)
    account_type = get_input("What would you like, Savings or Current?: ", clean_account_type, validate_account_type)

    acct = Account(first_name, last_name, email, phone_number, account_type)
    print(acct)

def run_tests():
    pass

def main():
    register()

if __name__ == "__main__":
    main()