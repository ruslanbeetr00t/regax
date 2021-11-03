import re

def try_use_regax():
    try:
        number = input('add phone')
        phone_number = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
        my = phone_number.search(f'My phone number: {number}')
        print('phone:' + my.group())
        print(type(my))
        if len(str(my.group())) == 10:
            print('ok')
    except TypeError:
        print('Будьте уважнішим')

try_use_regax()