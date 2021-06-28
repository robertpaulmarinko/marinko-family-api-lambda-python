import auth
import json

print("validate password:")
password = input("Enter the password to test:")
result = auth.attempt_login('{\n\t"password": "' + password + '"\n}')
print("result is:")
print(result)

print("validate token:")
token = input("Enter the token to test:")
token_result = auth.is_token_valid(token)
print("result is:")
print(token_result)

