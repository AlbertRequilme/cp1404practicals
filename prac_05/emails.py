"""
Emails
Estimated Time: ~35+ Minutes
Actual Time: 41 Minutes
"""


def main():
    """This function will prompt the user for their email, store them, and confirm if it's correct"""
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if correct_name not in ('', 'y', 'yes'):
            name = input("Name: ")
        emails_to_names[email] = name
        email = input("Email: ")
    print("\nStored Emails and Names:")
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """This function will split parts of the email to readable names"""
    name_part = email.split('@')[0]
    parts = name_part.split('.')
    name = " ".join(parts).title()
    return name


main()
