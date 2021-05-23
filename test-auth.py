import auth
import json

print("starting...")
password = input("Enter the password to test:")
result = auth.attempt_login('{\n\t"password": "' + password + '"\n}')
print("result is:")
print(result)
