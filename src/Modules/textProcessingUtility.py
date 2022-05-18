from googletrans import Translator
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import timeit
from tqdm import tqdm

def translateText(textArr,srcLanguage,destLanguage='en'):
    translator = Translator()
    resultArr = []
    for innerArr in tqdm(textArr):
        result = translator.translate(innerArr,src=srcLanguage,dest=destLanguage)
        resultInner = []
        for text in result:
            resultInner.append(text.text)
        resultArr.append(resultInner)
    return resultArr

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
                        test = x.split(" ")
                        test = [x for x in test if not has_numbers(x)]
                                    
                        tempArr.append(" ".join(test))

        if len(tempArr) > 0:
            result.append(tempArr)
    return result

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def any_curr(s, curr="¥$€£"):
    return any(c in s for c in curr)