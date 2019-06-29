import ocrspace

api = ocrspace.API()
print(api.ocr_url('https://images-na.ssl-images-amazon.com/images/I/71ovNJN1URL._SL1244_.jpg'))
print(api.ocr_url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Solid_blue.svg/225px-Solid_blue.svg.png'))
