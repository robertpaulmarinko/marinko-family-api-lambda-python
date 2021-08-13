import file_storage
import json
import uuid

"""
Sample of the recipe-box.json data structure

{
    "recipes": [
        {
            "id": "f9eb9e35-e34b-47c3-afe0-8fca2c36de91",
            "name": "Hamburgers on the grill",
            "source": "None",
            "instructions": null,
            "imageStorageKey": "f9eb9e35-e34b-47c3-afe0-8fca2c36de91.jpg"
        }
    ]
}
"""

# Key to the recipe JSON file in S3
RECIPE_JSON_KEY = 'menu/recipe-box.json'

def get_recipes():
    fileString = file_storage.get_file(file_storage.FAMILY_WEB_SITE_BUCKET, RECIPE_JSON_KEY)
    # print("Recipe file: " + fileString)

    return fileString

# Adds or updates a single recipe record
def save_recipe(recipeRequest):
    print("save_recipe: " + recipeRequest)

    # allRecipes in a Dictionary
    allRecipes = json.loads(get_recipes())

    # parse the incoming string into JSON
    recipeJson = json.loads(recipeRequest)

    # if id is empty, then add a new recipe,
    # otherwise, update the existing recipe
    id = recipeJson.get("id");
    print("id:" + id)
    if id == "":
        # add a new recipe to end of the array
        print("add as new recipe")
        id = uuid.uuid4().hex
        recipeJson["id"] = id
        allRecipes["recipes"].append(recipeJson)
    else:
        # look for existing recipe and replace in array
        for index, recipe in enumerate(allRecipes["recipes"], start=0):
            if recipe["id"] == id:
                print("Updating recipe at index: ", index)
                allRecipes["recipes"][index] = recipeJson

    # Deserialize recipe dictionary to JSON string and save to S3
    allRecipesJson = json.dumps(allRecipes)
    file_storage.put_file(file_storage.FAMILY_WEB_SITE_BUCKET, RECIPE_JSON_KEY, allRecipesJson)

    # Log action and return
    print(allRecipesJson)
    return allRecipesJson
