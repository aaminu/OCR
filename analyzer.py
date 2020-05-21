"""
performs Analysis and returns the Image with caption
"""

# import libraries
import os
import requests
from PIL import Image
from io import BytesIO
from auth import auth_env
import matplotlib.pyplot as plt


def analyzer(file_name=None, file_url=None):
    """ post to API for response"""

    endpoint, subscription_key = auth_env()

    # OCR link and parameters
    ocr_link = endpoint + "vision/v2.0/analyze"
    parameters = {"visualFeatures": 'Adult,Categories,Description,Objects,Tags'}

    if file_name:
        file_path = '~/Desktop/' + file_name
        file = os.path.expanduser(file_path)
        file_data = open(file, 'rb').read()
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


def plotter(results, save_img=False, file_name=None, file_url=None):
    """Display picture with caption and can save as well"""

    caption = results["description"]["captions"][0]["text"].capitalize()  # Access the line

    if file_name:
        file_path = '~/Desktop/' + file_name
        file = os.path.expanduser(file_path)
        image_ = Image.open(file)

    elif file_url:
        image_ = Image.open(BytesIO(requests.get(file_url).content))

    # Display the image and overlay it with the caption.
    plt.imshow(image_)
    _ = plt.title(caption, size="x-large", y=-0.1)
    plt.axis("off")
    if save_img:
        plt.savefig('analyzed.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    query = ''
    vals = ['d', 'o']

    while not query.lower() in vals:
        try:
            query = input('\nHello, do wish to analyze from your desktop or an online image.\nFor Desktop, please enter'
                          ' D and press Enter.\nFor online image, please enter O and press Enter'
                          '\nInput your preference here: ')

            assert query.lower() in vals

        except AssertionError:
            print('\nInput error, Please re-enter your option correctly\n')

    if query.lower() == 'd':
        print('\nPlease copy file to your desktop.\n')
        image = input('\nPlease enter file name with extension(e.g "fireflies.jpg"): ')
        save = input('\nWould you like to save the new picture [y/n]: ').lower().startswith('y')
        results = analyzer(file_name=image)
        plotter(results, file_name=image, save_img=save)

    else:
        url = input('\nPlease enter file-url: ')
        save = input('\nWould you like to save the new picture [y/n]: ').lower().startswith('y')
        results = analyzer(file_url=url)
        plotter(results, file_url=url, save_img=save)
