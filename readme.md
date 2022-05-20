## 1.Project Name
Menucard translator & visualizer
## 2. Short Description
We have experienced that some places abroad doesn’t have menu cards in a language that you understand, and you end up using google translate for every dish – which is time consuming.
We have therefore built an application that analyzes the text, finds illustrations of each dish and translates the text to a user specified language and consolidates it into a single PDF file.
## 3. List of used technologies
* Python
* tesseract
* tqdm
* p_tqdm
* OpenCV
* Multiprocessing
* Numpy
* Pandas
* iso639
* Googletrans
* fpdf
* cv2
* icrawler
## 4. Installation guide (if any libraries need to be installed)
Based on the assumption that you are running the standard docker build for the Python course..
Please add below to the standard dockerfile:
* `pip install pytesseract`
* `apt install tesseract-ocr-all -y` (must be run as root)
* `pip install googletrans==3.1.0a0`
* `pip install fpdf`
* `pip install icrawler`
* `pip install p_tqdm`
* `pip install iso639-lang`
## 5. User guide (how to run the program)
 1. Go to `src` folder
 2. execute `python main.py -h` and follow instructions
3. Once code is finished, open `result.pdf` in your favorite PDF viewer
## 6. Status (What has been done (and if anything: what was not done))
 We reached the main goals of the project set from the beginning, but did not manage to do the "nice to have" features.

 - :white_check_mark: Read the picture and convert it to text.
 - :white_check_mark: Translate the text to English or possibly a user preferred language.
 - :white_check_mark: Find online images of the dishes.
 - :white_check_mark: Create an illustration containing translated text and related images.
 - :x: Analyze whether the dish is vegetarian or not.
 - :x: Create a python backend to execute the application and upload images instead of running it all locally with local stored images.

 So we have built a CLI application that takes 3 mandatory arguments and 1 optional argument:

 **Mandatory:**
  1. `src` (The path of the file to analyze)
  2. `src_lang` (The language that the menucard is written in)
  3. `dest_lang` (The language you want it translated to)

 **Optional:**
  1. `-a` OR `--pic_amount` (The number of pictures you want of each dish)

Then we are pre-processing the image, analyzing it for text, pre-processing the text, finding dishes based on the text and translating the text before finally building the output PDF.


## 7. List of Challenges you have set up for your self (The things in your project you want to highlight)

TBD


