import cv2
import pytesseract
import numpy as np
import cv2
from scipy.ndimage import interpolation as inter
from p_tqdm import p_map


#To avoid any racecondition with tesseract
import os
os.environ['OMP_THREAD_LIMIT'] = '1'



def get_text(image_path,language=None):
 
    # Read image from which text needs to be extracted
    img = cv2.imread(image_path)
    base_img = img.copy()

    # Preprocessing the image starts
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours = get_contours(gray)
    
    #This function is to stay in the get_text function as we are using variables like img and base_img
    def get_text_from_contours(cnt):
        #Use area to sort out small/invalid crops in picture
        area = cv2.contourArea(cnt)
        if(area < 20000 and area > 400):
          
            x,y,w,h = cv2.boundingRect(cnt)
                
            # Cropping the text block for giving input to OCR
            cropped = img[y-2:y + h+2, x-2:x + w+2]

            #Resize to make sure letters is sufficient size for tesseract to detect
            resized = cv2.resize(cropped, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

            #correct any sceww
            corrected_skew = correct_skew(resized)[1]
            
            #preprocess the cropped image corrected for scew to improve readability 
            gray = cv2.cvtColor(corrected_skew, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
            
            #visual of image feeded to tesseract
            cv2.imwrite("../outputImages/"+str(area)+".png", thresh)
            
            # Drawing a bounding rectangle on copied image (NOT WORKING WITH MULTIPROCESS - RACE CONDITION)
            cv2.rectangle(base_img, (x, y), (x + w, y + h), (0, 255, 160), 2)
                
            # Apply OCR on the cropped image
            if(language == None):
                text = pytesseract.image_to_string(thresh)
            else:
                text = pytesseract.image_to_string(thresh, lang=language)
           
            return text

    
    
    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
   
    #Standard slow way
    #Creates array for appending text - only used if using old traditional way
    #result = []
    #for cnt in contours:
    #    result.append(get_text_from_contours(cnt))
    
    #Multiprocess 
    result = p_map(get_text_from_contours,contours)

  
    image_name = image_path.split('/')[-1]

    #Green boxes does not come on when multiprocessing because of race condition
    cv2.imwrite('../outputImages/'+image_name, base_img)
    

    # to remove any None values in list
    result = [i for i in result if i]

    #Reverses to get text in correct order
    return result[::-1]


def get_contours(gray_image):
    #Preprocess to make textareax float together
    thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
    cv2.imwrite('../outputImages/thresh.jpg', thresh)
    

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    #Dilate to make the areas more bold and detectable
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 5))
    dilate = cv2.dilate(thresh, kernel, iterations = 1)
    cv2.imwrite('../outputImages/dilate.jpg', dilate)

    #find contours
    contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    return (contours)


def correct_skew(image, delta=1, limit=5):
    def determine_score(arr, angle):
        data = inter.rotate(arr, angle, reshape=False, order=0)
        histogram = np.sum(data, axis=1)
        score = np.sum((histogram[1:] - histogram[:-1]) ** 2)
        return histogram, score

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 

    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    for angle in angles:
        histogram, score = determine_score(thresh, angle)
        scores.append(score)

    best_angle = angles[scores.index(max(scores))]

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, 
              borderMode=cv2.BORDER_REPLICATE)

    return best_angle, rotated


