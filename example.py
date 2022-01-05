import ocrspace
from ocrspace import Engine
import requests

# api with the default ocrengine aka engine 1
api = ocrspace.API()

# api with engine 2
api_with_engine_two = ocrspace.API(engine=Engine.ENGINE_2)
TEST_IMAGE_URL = 'https://images-na.ssl-images-amazon.com/images/I/71ovNJN1URL._SL1244_.jpg'

print('Testing URL-based OCR:')
print(api.ocr_url(TEST_IMAGE_URL))
print('Testing URL-based OCR using engine_two:')
print(api_with_engine_two.ocr_url(TEST_IMAGE_URL))

# Download image for demo purposes
TEST_FILENAME = '/tmp/test_image.jpg'
with open(TEST_FILENAME, 'wb') as f:
    r = requests.get(TEST_IMAGE_URL)
    r.raw.decode_content = True
    f.write(r.content)

print('Testing file-based OCR:')
# With file path
print(api.ocr_file(TEST_FILENAME))
# With file pointer
print(api.ocr_file(open(TEST_FILENAME, 'rb')))

print('Testing file-based OCR using engine_two:')
# With file path
print(api_with_engine_two.ocr_file(TEST_FILENAME))
# With file pointer
print(api_with_engine_two.ocr_file(open(TEST_FILENAME, 'rb')))
