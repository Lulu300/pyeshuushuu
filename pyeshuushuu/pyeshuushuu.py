from .image import Image


class PyEshuushuu(object):

    def __init__(self):
        self.url = 'http://e-shuushuu.net'

    def images(self, page=1):
        url = '{0}/?page={1}'.format(self.url, page)
        return Image.get_images(self.url, url)

    def search(self, tags=[], page=1):
        if tags is not isinstance(list()) or len(tags) < 1:
            raise Exception('tags must be a list with a least one tag')
        tags_str = '+'.join(tags)
        url = '{0}search/results/?page={1}&tags={2}'.format(self.url, page, tags_str)
        return Image.get_images(self.url, url)
