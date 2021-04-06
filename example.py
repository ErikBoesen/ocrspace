import ocrspace
import requests


api = ocrspace.API()
TEST_IMAGE_URL = 'https://images-na.ssl-images-amazon.com/images/I/71ovNJN1URL._SL1244_.jpg'

print('Testing URL-based OCR:')
print(api.ocr_url(TEST_IMAGE_URL))

print('Testing file-based OCR:')
# Download image for demo purposes
TEST_FILENAME = '/tmp/test_image.jpg'
with open(TEST_FILENAME, 'wb') as f:
    r = requests.get(TEST_IMAGE_URL)
    r.raw.decode_content = True
    f.write(r.content)

# With file path
print(api.ocr_file(TEST_FILENAME))
# With file pointer
print(api.ocr_file(open(TEST_FILENAME, 'rb')))
