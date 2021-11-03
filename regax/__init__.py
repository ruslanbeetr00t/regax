import re

def try_use_regax():
    number = input('add phone')
    phone_number = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
    my = phone_number.search(f'My phone number: {number}')
    print('phone:' + my.group())
    print(type(my))
    if len(str(my.group())) == 10:
        print('ok')
    else:
        return try_use_regax()

try_use_regax()