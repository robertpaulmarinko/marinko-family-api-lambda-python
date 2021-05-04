import lambda_function
import json

print("starting...")
lambda_function.lambda_handler(json.loads('{ "path": "/recipes", "multiValueHeaders": { "origin": ["https://beta.marinkofamily.com"] } }'), {})
