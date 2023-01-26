from new_user import *
from Validator import *
print("Welcome ")
key = input("Press 1 to add user and 2 for authentication check : ")
if key =='1':
    print('Loading to admin panel... ')
    uid()
elif key == '2':
    print('Redirecting for authentication check...  ')
    Validator()
else:
    print('Invalid output')