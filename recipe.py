import file_storage

def get_recipes():
    fileString = file_storage.get_file(file_storage.FAMILY_WEB_SITE_BUCKET, 'menu/recipe-box.json')
    print("Recipe file: " + fileString)

    return fileString
