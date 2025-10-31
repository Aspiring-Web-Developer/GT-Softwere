import re
strpassword=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&])[a-zA-Z\d@#$&]{8,}$'
paswrd='deept@k123'


if re.match(strpassword,paswrd):
    print('valid password')
else:
    print('invalid password')