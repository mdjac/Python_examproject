from googletrans import Translator

def translateText(textArr,srcLanguage='es',destLanguage='en'):
    translator = Translator()

    for innerArr in textArr:
        for index, text in enumerate(innerArr):
            result = translator.translate(text,src=srcLanguage,dest=destLanguage).text
            innerArr[index] = result
               
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
                    if not any_curr(x):           
                        tempArr.append(x)
                        
        if len(tempArr) > 0:
            result.append(tempArr)
    return result

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def any_curr(s, curr="¥$€£"):
    return any(c in s for c in curr)