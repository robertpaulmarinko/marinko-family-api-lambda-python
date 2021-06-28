import file_storage

def get_video_of_the_day_data():
    fileString = file_storage.get_file(file_storage.FAMILY_WEB_SITE_BUCKET, 'video-of-the-day-index.json')
    print("Video of the day file: " + fileString)

    return fileString
