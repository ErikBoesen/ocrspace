import requests
from enum import (Enum, unique)


class Language:
    Arabic = 'ara'
    Bulgarian = 'bul'
    Chinese_Simplified = 'chs'
    Chinese_Traditional = 'cht'
    Croatian = 'hrv'
    Danish = 'dan'
    Dutch = 'dut'
    English = 'eng'
    Finnish = 'fin'
    French = 'fre'
    German = 'ger'
    Greek = 'gre'
    Hungarian = 'hun'
    Korean = 'kor'
    Italian = 'ita'
    Japanese = 'jpn'
    Norwegian = 'nor'
    Polish = 'pol'
    Portuguese = 'por'
    Russian = 'rus'
    Slovenian = 'slv'
    Spanish = 'spa'
    Swedish = 'swe'
    Turkish = 'tur'


@unique
class Engine(Enum):
    """
    Engine: Enum representing the OCR engine to use
    """
    ENGINE_1 = 1
    ENGINE_2 = 2


class API:
    def __init__(
        self,
        endpoint='https://api.ocr.space/parse/image',
        api_key='helloworld',
        language=Language.English,
        engine=Engine.ENGINE_1,
        **kwargs,
    ):
        """
        :param endpoint: API endpoint to contact
        :param api_key: API key string
        :param language: document language
        :param ocrengine: ocr engine to use
        :param **kwargs: other settings to API
        """
        if not isinstance(engine, Engine):
            raise TypeError(
                "engine must be an instance of Engine"
            )
        if engine.value != 1 and engine.value != 2:
            raise ValueError(
                "the value of engine must be either 1 or 2, import & use ocrspace.Engine"
            )
        self.endpoint = endpoint
        self.payload = {
            'isOverlayRequired': True,
            'apikey': api_key,
            'language': language,
            'OCREngine': engine.value,
            **kwargs
        }

    def _parse(self, raw):
        if type(raw) == str:
            raise Exception(raw)
        if raw['IsErroredOnProcessing']:
            raise Exception(raw['ErrorMessage'][0])
        return raw['ParsedResults'][0]['ParsedText']

    def query_api(self, url_data=None, image_file=None):
        """
        Process the provided parameter.
        :param url_data: Either an Image url or base64image
        :param image_file: A path or file pointer to the image file
        :return: Result in JSON format
        :raise: request.exceptions or general Exception
        """
        if image_file:
            r = requests.post(
                self.endpoint,
                files={'filename': image_file},
                data=self.payload,
                timeout=30
            )
        if url_data:
            r = requests.post(
                self.endpoint,
                data=url_data,
                timeout=30
            )
        r.raise_for_status()
        return self._parse(r.json())

    def ocr_file(self, fp):
        """
        Process image from a local path.
        :param fp: A path or pointer to your file
        :return: Result in JSON format
        """
        with (open(fp, 'rb') if type(fp) == str else fp) as f:
            return self.query_api(image_file=f)

    def ocr_url(self, url):
        """
        Process an image at a given URL.
        :param url: Image url
        :return: Result in JSON format.
        """
        data = self.payload
        data['url'] = url
        return self.query_api(url_data=data)

    def ocr_base64(self, base64image):
        """
        Process an image given as base64.
        :param base64image: Image represented as Base64
        :return: Result in JSON format.
        """
        data = self.payload
        data['base64Image'] = base64image
        return self.query_api(url_data=data)
