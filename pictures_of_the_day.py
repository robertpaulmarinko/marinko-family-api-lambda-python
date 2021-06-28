import file_storage

def get_pictures_of_the_day_data():
    fileString = file_storage.get_file(file_storage.FAMILY_WEB_SITE_BUCKET, 'picture-of-the-day-index.json')
    print("Picture of the day file: " + fileString)

    return fileString
