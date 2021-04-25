import lambda_function
import json

print("starting...")
lambda_function.lambda_handler(json.loads('{ "path": "/videoOfTheDay/data" }'), {})
