# Import required packages
import os
import shutil
from Modules import imageProcessingUtility as ipu
from Modules import textProcessingUtility as tpu
from Modules import googleImageSearchUtility as gis
from Modules import pdfUtility as pdf
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import timeit
from pprint import pprint
from tqdm import tqdm

spanish = "../images/Spanish_menucard.jpg"
spanish2 = "../images/Spanish_menucard2.png"
spanish3 = "../images/Spanish_menucard3.jpeg"

start = timeit.default_timer()
#Cleaner folders
outputImages = "../outputImages"
temp_search_images = "../temp_search_images"

print("-----------------------------------------------------")
print("Cleaning up directories")
try:
    shutil.rmtree(outputImages)
    os.mkdir(outputImages)
    shutil.rmtree(temp_search_images)
    os.mkdir(temp_search_images)
except OSError as e:
    print("Error:" + e.strerror)


print("-----------------------------------------------------")
print("Starting image processing")
rawText = ipu.get_text(spanish,language="spa")


print("-----------------------------------------------------")
print("ORIGINAL TEXT!")
pprint(rawText)


print("-----------------------------------------------------")
formattedText = tpu.formatText(rawText)
print("FORMATTED TEXT!")
pprint(formattedText)


#Downloads the images
print("-----------------------------------------------------")
print("Starting image downloading from google")
with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
    res = list(tqdm(ex.map(gis.downloadImages,[i[0] for i in formattedText],range(len(formattedText))),total=len(formattedText)))


#Below is for measuring the download speed without multiprocessing.
''' start = timeit.default_timer()
for index, text in enumerate(formattedText):
    gis.downloadImages(text[0],index)
stop = timeit.default_timer()
print('Time without multi process: ', stop - start)  '''


print("-----------------------------------------------------")
print("Starting text translation")
formattedText_copy = formattedText.copy()
translatedText = tpu.translateText(formattedText,"es","da")
print("TRANSLATED TEXT!")
pprint(translatedText)


output = []
for index, item in enumerate(formattedText_copy):
    output.append({'original': item, 'translated': translatedText[index]})
    

print("-----------------------------------------------------")
print("Creating PDF")
pdf.createPDF(output)


stop = timeit.default_timer()
print("-----------------------------------------------------")
print('Total runtime: ', stop - start)



    



