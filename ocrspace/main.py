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
            raise TypeError(
                "ocrengine must be an instance of OCREngine_VAL enum class"
            )
        if ocrengine.value != 1 and ocrengine.value != 2:
            raise ValueError(
                "the value of ocrengine must be either 1 or 2, import & use ocrspace.OCREngine_VAL"
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

    def query_api(self, url_data=None, pic_file=None):
        """
        Process the provided parameter.
        :param url_data: Either an Image url or base64image
        :param pic_file: A path or pointer to image file
        :return: Result in JSON format
        :raise: request.exceptions or general Exception
        """
        try:
            if pic_file:
                r = requests.post(
                    self.endpoint,
                    files={'filename': pic_file},
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
        except requests.exceptions.Timeout as time_out:
            raise time_out
        except requests.exceptions.TooManyRedirects as too_man_redirects:
            raise too_man_redirects
        except requests.exceptions.HTTPError as http_error:
            raise http_error
        except requests.exceptions.RequestException as request_exception:
            raise request_exception
        except Exception as e:
            raise e
        else:
            return self._parse(r.json())

    def ocr_file(self, fp):
        """
        Process image from a local path.
        :param fp: A path or pointer to your file
        :return: Result in JSON format
        """
        with (open(fp, 'rb') if type(fp) == str else fp) as f:
            return self.query_api(pic_file=f)

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
