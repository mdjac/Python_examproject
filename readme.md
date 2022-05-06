## Group name and group members.
Christian & Mikkel. Members: Christian Rosenbæk & Mikkel Jacobsen

## Description of the data (with a link to the data source)
Data will be images of menu cards in foreign language(s).

## Description of the proplem (what questions to ask the data)
We have experienced that some places abroad doesn’t have menu cards in a language that you understand, and you end up using google translate for every dish – which is time consuming.
We will build an application that will analyze the text in the picture and translate it to English and show illustrations of each dish based on online queries – to get a visual overview.

## What technologies (libraries) will be used
We are not 100% sure which libraries yet, but some initial thoughts ends up at:
Pytesseract, Keras-OCR, OpenCV, Pandas, Numpy, Matplotlib, Selenium, Beautiful soup, Flask/Django, NLTK, googletrans.

## What will be the main challenge(s) in the project
The main challenges is written in prioritized order below:
1. Read the picture and convert it to text.
2. Translate the text to English or possibly a user preferred language.
3. Find online images of the dishes.
4. Create an illustration containing translated text and related images.
5. Analyze whether the dish is vegetarian or not.
6. Create a python backend to execute the application and upload images – instead of running it all        locally with local stored images.


## Required libraries.
Insert below to dockerfile
- pip install pytesseract
- apt install tesseract-ocr-all -y (must be run as root)
