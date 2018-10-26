from pyeshuushuu import PyEshuushuu
from pyeshuushuu.downloader import Downloader

pyeshuushuu = PyEshuushuu()
images = pyeshuushuu.images()
Downloader.download_images(images, '/home/lulu/Pictures/eshuushuu')
