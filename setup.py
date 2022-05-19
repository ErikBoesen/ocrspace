from distutils.core import setup

setup(
    name='ocrspace',
    packages=['ocrspace'],  # this must be the same as the name above
    requires=['requests'],
    version='2.3.0',
    description='Perform OCR through ocr.space API',
    author=['Ali Najafi', 'Erik Boesen', 'Negassa Berhanu'],
    author_email='forpurposes1435@gmail.com',
    url='https://github.com/ErikBoesen/ocrspace',
    keywords=['ocr'],
    classifiers=[],
)
