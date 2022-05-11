from googletrans import Translator

translator = Translator()

translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

for translation in translations:
    print(translation.origin, ' -> ', translation.text)