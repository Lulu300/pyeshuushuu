import click
import os
import requests
import time


class Downloader(object):

    @staticmethod
    def download_image(image, folder):
        filename = image['url'].split('/')[-1]
        file = os.path.join(folder, filename)
        if os.path.exists(file):
            return True
        label = 'Downloading {0}'.format(file)
        response = requests.get(image['url'], stream=True)
        total_size = int(response.headers.get('content-length'))
        with open(file, 'wb') as file_content:
            with click.progressbar(length=total_size, label=label) as bar:
                for data in response.iter_content(chunk_size=int(total_size / 5)):
                    file_content.write(data)
                    bar.update(len(data))

    @staticmethod
    def download_images(images, folder):
        with click.progressbar(length=len(images), label='Downloading files') as bar:
            for image in images:
                already_download = Downloader.download_image(image, folder)
                bar.update(1)
                if not already_download:
                    time.sleep(0.5)
