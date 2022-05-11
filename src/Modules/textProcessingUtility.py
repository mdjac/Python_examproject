from googletrans import Translator
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import timeit


def translateText(textArr,srcLanguage,destLanguage='en'):
    translator = Translator()
    for innerArr in textArr:
        result = translator.translate(innerArr,src=srcLanguage,dest=destLanguage)
        for index, text in enumerate(innerArr):
            innerArr[index] = result[index].text
    return textArr

def formatText(textArray):
    result = []
    for text in textArray:
        temp = text.split("\n")
        tempArr = []
        for t in temp:
            x = t.strip()
            if x != "":
                try:
                    #replace , with .
                    y = x.replace(",",".")
                    float(y)
                except:
                    if not any_curr(x) and len(x)>4:           
                        tempArr.append(x)

        if len(tempArr) > 0:
            result.append(tempArr)
    return result

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def any_curr(s, curr="¥$€£"):
    return any(c in s for c in curr)