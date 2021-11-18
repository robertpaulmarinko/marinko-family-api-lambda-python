import file_storage

upload_url = file_storage.create_presigned_upload_url('family-web-site-recipe-images', 'keyvalue', 600, 'image/jpeg');
print('Upload URL:')
print(upload_url)

down_url = file_storage.create_presigned_download_url('family-web-site-recipe-images', '79cd6f16b99f4980813a09cbca1fe8b2.jpg', 600);
print('Download URL:')
print(down_url)
