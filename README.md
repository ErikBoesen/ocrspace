# `ocrspace`

> A Python wrapper for using the [ocr.space API](https://ocr.space/ocrapi).

## Installation

Simply install from `pip`:

```sh
pip install ocrspace
```

## Use

First you'll need to import and instantiate the API wrapper:

```python
import ocrspace
api = ocrspace.API()
# Or if you have a custom API host, API key or desired language, pass those:
api = ocrspace.API(endpoint='https://example.host', api_key='Insert key here', language=ocrspace.Language.Croatian)
```

If you wish to change the OCR used, you'll have to import the enum class OCREngine_VAL from ocrspace and pass the value of OCREngine_VAL.val_2 to the api instantiation. By default it uses OCREngine_VAL.val_1:

```python
import ocrspace
from ocrspace import OCREngine_VAL
api = ocrspace.API(ocrengine=OCREngine_VAL.val_2)
# Or if you have a custom API host, API key or desired language, pass those:
api = ocrspace.API(endpoint='https://example.host', api_key='Insert key here', language=ocrspace.Language.Croatian, ocrengine=OCREngine_VAL.val_2)
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
