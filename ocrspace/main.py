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
class OCREngine_VAL(Enum):
    """
    OCRengine_VAL: the OCRengine to use, values can only be 1 or 2

    Args:
        Enum: python's generic enumeration that is used to define new enumerations.
    """
    engine_1 = 1
    engine_2 = 2


class API:
    def __init__(
        self,
        endpoint='https://api.ocr.space/parse/image',
        api_key='helloworld',
        language=Language.English,
        ocrengine=OCREngine_VAL.engine_1,
        **kwargs,
    ):
        """
        :param endpoint: API endpoint to contact
        :param api_key: API key string
        :param language: document language
        :param ocrengine: ocr engine to use
        :param **kwargs: other settings to API
        """
        if not isinstance(ocrengine, OCREngine_VAL):
            raise ValueError(
                "the value of ocrengine must be an instance of OCREngine_VAL enum class"
            )
        if ocrengine.value != 1 and ocrengine.value != 2:
            raise Exception(
                "the value of ocrengine must be either 1 or 2, import & use OCREngine_VAL"
            )
        self.endpoint = endpoint
        self.payload = {
            'isOverlayRequired': True,
            'apikey': api_key,
            'language': language,
            'OCREngine': ocrengine.value,
            **kwargs
        }

    def _parse(self, raw):
        if type(raw) == str:
            raise Exception(raw)
        if raw['IsErroredOnProcessing']:
            raise Exception(raw['ErrorMessage'][0])
        return raw['ParsedResults'][0]['ParsedText']

    def ocr_file(self, fp):
        """
        Process image from a local path.
        :param fp: A path or pointer to your file
        :return: Result in JSON format
        """
        with (open(fp, 'rb') if type(fp) == str else fp) as f:
            r = requests.post(
                self.endpoint,
                files={'filename': f},
                data=self.payload,
            )
        return self._parse(r.json())

    def ocr_url(self, url):
        """
        Process an image at a given URL.
        :param url: Image url
        :return: Result in JSON format.
        """
        data = self.payload
        data['url'] = url
        r = requests.post(
            self.endpoint,
            data=data,
        )
        return self._parse(r.json())

    def ocr_base64(self, base64image):
        """
        Process an image given as base64.
        :param base64image: Image represented as Base64
        :return: Result in JSON format.
        """
        data = self.payload
        data['base64Image'] = base64image
        r = requests.post(
            self.endpoint,
            data=data,
        )
        return self._parse(r.json())
