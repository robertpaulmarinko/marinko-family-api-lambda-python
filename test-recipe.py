import lambda_function
import json
import recipe

recipe.save_recipe('''
        {
            "id": "f9eb9e35-e34b-47c3-afe0-8fca2c36de91",
            "name": "Hamburgers on the grill - change 1",
            "source": "None",
            "instructions": null,
            "imageStorageKey": "f9eb9e35-e34b-47c3-afe0-8fca2c36de91.jpg"
        }
''')

recipe.save_recipe('''
        {
            "id": "",
            "name": "New recipe 1",
            "source": "None",
            "instructions": null,
            "imageStorageKey": ""
        }
''')

print("starting...")
lambda_function.lambda_handler(json.loads('{ "path": "/recipes", "multiValueHeaders": { "origin": ["https://beta.marinkofamily.com"] } }'), {})

