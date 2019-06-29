import ocrspace

api = ocrspace.API()
from pprint import pprint
pprint(api.ocr_url('https://images-na.ssl-images-amazon.com/images/I/71ovNJN1URL._SL1244_.jpg'))
pprint(api.ocr_url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Batian_Nelion_and_pt_Slade_in_the_foreground_Mt_Kenya.JPG/220px-Batian_Nelion_and_pt_Slade_in_the_foreground_Mt_Kenya.JPG'))
