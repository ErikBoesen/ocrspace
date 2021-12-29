# `ocrspace`

> A Python wrapper for using the [ocr.space API](https://ocr.space/ocrapi).

## Installation

Simply install from `pip`:

```sh
pip install ocrspace
```

## Use

Before anything else, you need to get your apikey from [Free OCR API](https://ocr.space/OCRAPI) otherwise the default apikey -- i.e **helloworld** -- will be used and according to the developers of [Free OCR API](https://ocr.space/faq#span12):
> This key is great for a quick test, but do not use it in your project, as it is severely rate limited.

First you'll need to import and instantiate the API wrapper:

```python
import ocrspace

api_key = "apikey retrieved from Free OCR API"

api = ocrspace.API(api_key=api_key)
# Or if you have a custom API host, API key or desired language, pass those:
api = ocrspace.API(endpoint='https://example.host', api_key=api_key, language=ocrspace.Language.Croatian)
```

If you wish to change the OCR engine used, you'll have to import the enum class OCREngine_VAL from ocrspace and pass the value of OCREngine_VAL.val_2 to the api instantiation. By default it uses OCREngine_VAL.val_1:

```python
import ocrspace
from ocrspace import OCREngine_VAL

api_key = "apikey retrieved from Free OCR API"

api = ocrspace.API(api_key=api_key, ocrengine=OCREngine_VAL.val_2)
# Or if you have a custom API host, API key or desired language, pass those:
api = ocrspace.API(endpoint='https://example.host', api_key=api_key, language=ocrspace.Language.Croatian, ocrengine=OCREngine_VAL.val_2)
```

To perform recognition on an image hosted at some URL:

```python
api.ocr_url('URL of image goes here')
```

Or, if you have an image locally upon which to perform recognition:

```python
api.ocr_file('image.jpg')
# or:
api.ocr_file(open('image.jpg', 'rb'))  # or any other file pointer
```

That's it! Look at [`example.py`](example.py) for a demonstration.

## Authorship

This package was created by [Ali Najafi](https://github.com/a4fr) and is maintained by [Erik Boesen](https://github.com/ErikBoesen).

## License

[MIT](LICENSE)
