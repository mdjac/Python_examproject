#from google_images_search import GoogleImagesSearch
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
from six.moves.urllib.parse import urlparse
import base64


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
    


def downloadImages(keyword, courseIndex, number=3):
    google_crawler = GoogleImageCrawler(downloader_cls=My_image_downloader, downloader_threads=number, storage={'root_dir': "../temp_search_images/"+str(courseIndex)+"/"}, log_level=100)
    google_crawler.crawl(keyword=keyword, max_num=number)



''' def searchImages(query, courseIndex, number=3):
    gis = GoogleImagesSearch('AIzaSyD4yxnDEF3QB02HjOPbu9XEHQUkt0A9-4Y', '9cf2302238126cb4b')
    _search_params = {
        'q': query,
        'num': number,
        'fileType': 'png',
    }
    gis.search(search_params=_search_params, path_to_dir="../temp_search_images/"+str(courseIndex)+"/" ,width=50, height=50)
  


    for index, image in enumerate(gis.results()):
        nparr = np.frombuffer(image.get_raw_data(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        #Makes sure all images have same height
        height = 250
        (h, w) = img.shape[:2]
        r = height / float(h)
        dim = (int(w * r), height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #Images done and kept in resized variable
        #cv2.imwrite("test"+str(index)+"_resize2.png",resized)
        print("it works") '''
