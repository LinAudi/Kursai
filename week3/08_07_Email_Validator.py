print("Email Validator: \n")



def email_validation(email):
    if email.count("@") == 1 and email.count(".") == 1:
        return True
    else:
        return False
email = input("Enter an email address: 'example@gmail.com': ")

if email_validation(email):
    print("The email address is valid.")
else:
    print("Unvalid email")


    # def validate_email(email):
    #     if email.count('@') != 1:
    #         return False
    #     username, domain = email.split('@')
    #     if not username:
    #         return False
    #     if '.' not in domain:
    #         return False
    #     domain_parts = domain.split('.')
    #     if any(len(part) == 0 for part in domain_parts[:-1]):
    #         return False
    #     # Ensure the domain suffix is at least 2 characters long
    #     if len(domain_parts[-1]) < 2:
    #         return False
    #     return True
    #
    #
    # email = input("Enter an email address: ")
    # if validate_email(email):
    #     print("The email address is valid.")
    # else:
    #     print("The email address is invalid.")






    # def validate_email(email):  # Example: mantas.skara@gmail.com
    #     # Check for exactly one '@' symbol
    #     if email.count('@') != 1:
    #         return False
    #
    #     # Split the email into username and domain
    #     username, domain = email.split('@')
    #
    #     # Validate the username
    #     if not username:
    #         return False
    #
    #     # Validate the domain
    #     if '.' not in domain:
    #         return False
    #
    #     # Split the domain into parts
    #     domain_parts = domain.split('.')
    #
    #     # Check each part of the domain except the last one
    #     for part in domain_parts[:-1]:
    #         if len(part) == 0:
    #             return False
    #
    #     # Ensure the domain suffix is at least 2 characters long
    #     if len(domain_parts[-1]) < 2:
    #         return False
    #
    #     return True
    #
    #
    # # Test the function with two example emails
    # email = "mantas.skara@gmail.com"
    # email2 = "faf"
    #
    # # Validate the first email
    # is_valid = validate_email(email)
    #
    # # Print the result
    # if is_valid:
    #     print("Valio")
    # else:
    #     print("Oh no")
    #
    # # Validate the second email
    # is_valid2 = validate_email(email2)
    #
    # # Print the result for the second email
    # if is_valid2:
    #     print("Valio")
    # else:
    #     print("Oh no")
