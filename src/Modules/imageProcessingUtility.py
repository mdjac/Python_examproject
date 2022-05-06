import cv2
import pytesseract
from tqdm import tqdm
def get_text(image_path,language=None):
    # Read image from which text needs to be extracted
    img = cv2.imread(image_path)

    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 5))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)

    #Creates array for appending text
    text_list = []

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    test = []
    for cnt in tqdm(contours):
        #Use area to sort out small/invalid crops in picture
        area = cv2.contourArea(cnt)
        if(area < 20000 and area > 400):
            x,y,w,h = cv2.boundingRect(cnt)
                
            # Drawing a rectangle on copied image
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 160), 2)
                
            # Cropping the text block for giving input to OCR
            cropped = img[y:y + h, x:x + w]
                
            # Apply OCR on the cropped image
            if(language == None):
                text = pytesseract.image_to_string(cropped)
            else:
                text = pytesseract.image_to_string(cropped, lang=language)
            #split text on backslash n
            test.append(text)
            text = text.split('\n')
            for t in text:
                t = t.strip()
                #only add if not empty
                if t != '':
                    text_list.append(t)
            
    for t in test:
        print(t)
    image_name = image_path.split('/')[-1]
    cv2.imwrite('../outputImages/'+image_name, img)
    #Reverses to get text in correct order
    return text_list[::-1]