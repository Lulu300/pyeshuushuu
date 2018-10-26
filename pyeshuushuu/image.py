import json
import requests
import re

from bs4 import BeautifulSoup


class Image(object):

    @staticmethod
    def get_image(image_div, base_url):
        image = dict()
        thumb = image_div.find('div', attrs={'class': 'thumb'})
        title = image_div.find('div', attrs={'class': 'title'})
        meta = image_div.find('div', attrs={'class': 'meta'})
        image['id'] = int(title.find('a').text.split('#')[-1].strip())
        image['url'] = '{0}{1}'.format(base_url, thumb.find('a', attrs={'class': 'thumb_image'})['href'].strip())
        image['thumbnail'] = '{0}{1}'.format(base_url, thumb.find('img')['src'].strip())
        image['date'] = meta.find('dt', text=re.compile('Submitted On:')).find_next_sibling('dd').text.strip()
        image['size'] = meta.find('dt', text=re.compile('File size:')).find_next_sibling('dd').text.strip()
        image['dimensions'] = meta.find('dt', text=re.compile('Dimensions:')).find_next_sibling('dd').text.split(' ')[0].strip()
        return image

    @staticmethod
    def get_images(base_url, url):
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        content = soup.find('div', attrs={'id': 'content'})
        images_div = content.find_all('div', attrs={'class': 'image_thread'})
        if images_div is None:
            return None
        images = list()
        for image_div in images_div:
            images.append(Image.get_image(image_div, base_url))
        return images
