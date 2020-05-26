"""
performs OCR and returns Text from File
"""

# import libraries
import os
import sys
import requests
from pathlib import Path
from auth import auth_env


def ocr(file_name=None, file_url=None):
    """ post to API for response"""

    endpoint, subscription_key = auth_env()

    # OCR link and parameters
    ocr_link = endpoint + "vision/v2.0/ocr"
    parameters = {"language": 'unk', "detectOrientation": True}

    if file_name:
        cwd = Path.cwd()
        file_path = Path(Path.joinpath(cwd.parent, file_name))
        file_data = open(file_path, 'rb').read()
        request_header = {"Content-Type": 'application/octet-stream', "Ocp-Apim-Subscription-Key": subscription_key}

        # Post to API
        response = requests.post(ocr_link, params=parameters, headers=request_header, data=file_data)
        response.raise_for_status()

        return response.json()

    elif file_url:
        data = {'url': file_url}
        request_header = {"Ocp-Apim-Subscription-Key": subscription_key}

        # Post to API
        response = requests.post(ocr_link, params=parameters, headers=request_header, json=data)
        response.raise_for_status()
        return response.json()

    else:
        sys.exit('Please provide either file-name or file-url')


def ocr_text_retriever(result):
    """Retrieval of text from OCR Json output using Microsoft Computer Vision API -  """

    line = result['regions'][0]['lines']  # Access the line
    text = []  # Placeholder

    def recurs_text(lst_):
        """ Recursive func through Line"""
        if not lst_:
            return text
        else:
            temp = lst_.pop(0)
            for item in temp['words']:
                text.append(item.get('text'))
            text.append('\n')
            return recurs_text(lst_)

    return ' '.join(recurs_text(line))


if __name__ == '__main__':
    query = ''
    vals = ['d', 'o']

    while not query.lower() in vals:
        try:
            query = input('\nHello, do wish to scan from your desktop or an online image.\nFor Desktop, please enter '
                          'D and press Enter.\nFor online image, please enter O and press Enter'
                          '\nInput your preference here: ')

            assert query.lower() in vals

        except AssertionError:
            print('\nInput error, Please re-enter your option correctly\n')

    if query.lower() == 'd':
        print('\nPlease copy file to your parent directory, e.g. Desktop, Documents...\n')
        image = input('\nPlease enter file name with extension(e.g "fireflies.jpg"): ')
        results = ocr(file_name=image)
        print('\nThe content of your document is:\n\n', ocr_text_retriever(results))

    else:
        url = input('\nPlease enter file-url: ')
        results = ocr(file_url=url)
        print('\nThe content of your document is:\n\n', ocr_text_retriever(results))
