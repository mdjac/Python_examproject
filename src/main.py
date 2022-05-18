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
import argparse
from iso639 import Lang
import numpy as np
import config


#source_language is 3 letter ex. spanish = spa
def translate_menucard(source_image_path,source_language, destination_language, pic_amount ):
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
    rawText = ipu.get_text(source_image_path,language=source_language.pt3)


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
        res = list(tqdm(ex.map(gis.downloadImages,[i[0] for i in formattedText],range(len(formattedText)), np.repeat(pic_amount,len(formattedText))),total=len(formattedText)))


    #Below is for measuring the download speed without multiprocessing.
    ''' start = timeit.default_timer()
    for index, text in enumerate(formattedText):
        gis.downloadImages(text[0],index)
    stop = timeit.default_timer()
    print('Time without multi process: ', stop - start)  '''


    print("-----------------------------------------------------")
    print("Starting text translation")
    formattedText_copy = formattedText.copy()
    translatedText = tpu.translateText(formattedText,source_language.pt1,destination_language.pt1)
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

if __name__ == "__main__":
    print("This is run from main")
    parser = argparse.ArgumentParser(description="Translates a menucard to a preferred language and fetches pictures of similar dishes")
    parser.add_argument("src",help='The path of the file to analyze: Format: ../images/Spanish_menucard.jpg')
    parser.add_argument("src_lang",help='The source language of the menucard. Format: Spanish, es or spa')
    parser.add_argument("dest_lang",help='The destination language of the menucard. Format: Spanish, es or spa')
    parser.add_argument("-a", "--pic_amount",help='The number of images to fetch for each dish', type=int, choices={1,2,3,4,5}, default=config.image_downloader['standard_pictures_amount'])
    args = parser.parse_args()
    source_file = args.src
    pic_amount = args.pic_amount
    source_lang = Lang(args.src_lang)
    destination_lang = Lang(args.dest_lang)
    translate_menucard(source_file,source_lang,destination_lang, pic_amount)

    



