# `ocrspace`

> A Python wrapper for using the [ocr.space API](https://ocr.space/ocrapi).

## Installation

Simply install from `pip`:

```sh
pip install ocrspace
```

## Use

First, get an API key from [Free OCR API](https://ocr.space/OCRAPI), otherwise the default apikey `helloworld` will be used, which is [severely rate limited.](https://ocr.space/faq#span12)

First you'll need to import and instantiate the API wrapper:

```python
import ocrspace

api_key = 'apikey retrieved from Free OCR API'

api = ocrspace.API(api_key=api_key)
# Or if you have a custom API host, API key or desired language, pass those:
api = ocrspace.API(endpoint='https://example.host', api_key=api_key, language=ocrspace.Language.Croatian)
```

If you wish to change the OCR engine used, use the enum class Engine from ocrspace and pass the value of ocrspace.Engine.Engine.ENGINE_2 to the api instantiation. By default it uses ocrspace.Engine.Engine.ENGINE_1:

```python
import ocrspace

api_key = "apikey retrieved from Free OCR API"

api = ocrspace.API(api_key=api_key, engine=ocrspace.Engine.Engine.ENGINE_2)
# Or if you have a custom API host, API key or desired language, pass those:
api = ocrspace.API(endpoint='https://example.host', api_key=api_key, language=ocrspace.Language.Croatian, engine=ocrspace.Engine.Engine.ENGINE_2)
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
