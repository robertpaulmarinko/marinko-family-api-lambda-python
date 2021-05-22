import auth
import json

print("starting...")
result = auth.attempt_login('{\n\t"password": "password"\n}')
print("result is:")
print(result)

result = auth.attempt_login('{\n\t"password": "bad"\n}')
print("result is:")
print(result)
