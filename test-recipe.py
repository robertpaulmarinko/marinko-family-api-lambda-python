import lambda_function
import json
import recipe

# WARNING - the save_recipe function will update the JSON file in S3
# Code is commented out, only run if you really want to update the S3 data
"""
recipe.save_recipe('''
        {
            "id": "2d31df47-c56f-44d1-b43d-91780862035f",
            "name": "Hot dogs change",
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
"""

print("starting...")
# lambda_function.lambda_handler(json.loads('{ "path": "/recipes", "multiValueHeaders": { "origin": ["https://beta.marinkofamily.com"] } }'), {})

recipes = recipe.get_recipes()
print(recipes)

