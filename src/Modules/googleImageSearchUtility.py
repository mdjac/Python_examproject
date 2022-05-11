from google_images_search import GoogleImagesSearch
from io import BytesIO
from PIL import Image
import cv2
import numpy as np


gis = GoogleImagesSearch('AIzaSyD4yxnDEF3QB02HjOPbu9XEHQUkt0A9-4Y', '9cf2302238126cb4b')



def searchImages(query,number=3):
    _search_params = {
        'q': query,
        'num': number,
        'fileType': 'jpg|jpeg|png',
    }
    gis.search(search_params=_search_params, width=500, height=500)
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
        print("it works")
