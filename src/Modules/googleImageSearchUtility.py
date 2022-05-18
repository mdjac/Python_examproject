import cv2
import numpy as np
from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
from six.moves.urllib.parse import urlparse
import base64
import config


class My_image_downloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        # works for python 3
        filename = base64.b64encode(url_path.encode()).decode()
        return '{}.{}'.format(filename, extension)
    


def downloadImages(keyword, courseIndex, number=config.image_downloader['standard_pictures_amount']):
    google_crawler = GoogleImageCrawler(downloader_cls=My_image_downloader, downloader_threads=number, storage={'root_dir': "../temp_search_images/"+str(courseIndex)+"/"}, log_level=100)
    google_crawler.crawl(keyword=keyword, max_num=number)


