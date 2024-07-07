'''
Написати функцію, яка буде перевіряти чи email адреса валідна та діставати юзернейм та домен
'''
import re

# example1@gmail.com
def validate_email(email_str: str) -> list[str]:
    # pattern = r'(\w+)@(\w+).([a-zA-Z]+)'
    # return re.fullmatch(pattern, email_str).groups()
    pattern = r'(?P<username>\w+)@(?P<domain>\w+).(?P<top_level_domain>[a-zA-Z]+)'
    return re.fullmatch(pattern, email_str).groupdict()

print(validate_email("example1@gmail.com"))
