from google_images_search import GoogleImagesSearch
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
from icrawler.builtin import GoogleImageCrawler





def downloadImages(keyword, courseIndex, number=3):
    google_crawler = GoogleImageCrawler(downloader_threads=number, storage={'root_dir': "../temp_search_images/"+str(courseIndex)+"/"})
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
