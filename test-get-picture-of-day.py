import lambda_function
import json

print("starting...")
lambda_function.lambda_handler(json.loads('{ "path": "/picturesOfTheDay/data", "multiValueHeaders": { "origin": ["https://beta.marinkofamily.com"] } }'), {})
