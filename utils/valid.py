import re


def validate_email(email):
    email_regex = r"/^[^\s@]+@[^\s@]+\.[^\s@]+$/"
    return re.match(email_regex, email)
