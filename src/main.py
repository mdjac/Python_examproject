# Import required packages
import os
import shutil
from Modules import imageProcessingUtility as ipu
from Modules import textProcessingUtility as tpu



spanish = "../images/Spanish_menucard.jpg"
spanish2 = "../images/Spanish_menucard2.png"
spanish3 = "../images/Spanish_menucard3.jpeg"


#Cleaner output images
dir_path = "../outputImages"
try:
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))


#rawText = ipu.get_text(spanish,language="spa")
#print(rawText)

tempText = ['para comer\n\x0c', 'carnes\n\x0c', 'tapas frias\n\x0c', '10,5\n\x0c', 'BURGER CLÁSICA (2208r8) !\ncon lechuga, cebolla, tomate. queso\ncheddar y pepiniíllos\n\x0c', '6.5\n\x0c', 'Sazño A y almendritas\n\x0c', '10,5\n\x0c', '6,5\n\x0c', 'BURGER MANOLETE (220gr8)\ncon jamón, queso manchego, cebolla,\nsalmorejo y lechuga\n\x0c', 'HUMMUS\ncon pan árabe\n\x0c', '75\n\x0c', 'MOUSSE DE FOIE (MI CUIT)\ncon mermelada de cerveza tostada y\nsalsa de violetas\n\x0c', '10.5\n\x0c', 'BURGER CORGONZOLA (220gr8)\ncon crema de queso gorgonzola,\ncebolla caramelízada y nueces\n\x0c', '8,5\n\x0c', "ENSALADA SIFONERA\nlochuguitas, jáminas de calabacin,\nCR 's, 541 negra, tomate seco\nsicrES de trufa blanca y\n\x0c", '10,5\n\x0c', 'SECRETO IBÉRICO\ncon espuma de euinness y regaliz,\ny patatas a la vtaíniila\n\x0c', '13,5\n\x0c', '8,5\n\x0c', 'ENSALADA CAPRESE\ncon tres tomates distintos, mozzarella\ny aceite de albahaca\n\x0c', 'LOMO DE TERNERA BRASEADO\ncon chimichurri y sus patatítas\n\x0c', '9,5\n\x0c', 'CARPACCIO DE PEZ MANTEQUILLA\ncon sal rosa, eneldo y helado de wasabi\n\x0c', 'woks\n\x0c', 'todos nuestros woks se sirven con noodles de\narroz, calabacín, zanahoria, pimiento rojo y\nverde, cebolla, sésamo, champiñón y nuestras\nsalsas secretas.\n\x0c', 'tapas calientes\n\x0c', '4,9\n\x0c', 'UNA DE BRAVAS\ncon la receta de mi madre. Puedes\npedirlas extrapicantes\n\x0c', '\x0c', 'VEGETAL\n\x0c', '5,9\n\x0c', 'GYOZAS JAPONESAS\nempanadillas orientales de pollo\ny verduras con salsa de soja\n\x0c', '\x0c', 'CON GAMBAS\n\x0c', '\x0c', 'CON POLLO\n\x0c', '9,9\n\x0c', 'CROQUETAS SIFONERAS\nlas hacemos de cecína, de gambón o\nvegetales con gorgonzola.\n\x0c', '\x0c', 'CON TERNERA\n\x0c', '6,5\n\x0c', 'postres\n\x0c', 'PROVOLETA AL HORNO\nqueso provolone horneado y\nrelleno de confíitura de tomate\n\x0c', '\x0c', 'TARTA DE QUESO\ncon arándanos o con dulce de leche\n\x0c', 'QUESADILLAS A LA ESPAÑOLA\ncon morcilla de burgos, queso\nidiazábal, manzana, miel y canela\n\x0c', '7,5\n\x0c', '\x0c', 'SUPER TORRIJA CASERA\ncon helado de leche merengada\n\x0c', '\x0c', 'PAN BAO DE RABO DE TORO\ncon rúcula, cebolla morada y\nmayonesa de Kinchee (Suas\n\x0c', 'TIRAMISÚ\n\x0c', '\x0c', 'COULANT DE CHOCOLATE\ncon salsa de chocolate blanco\n\x0c', '\x0c', '\x0c', 'DIM SUM DE CARRILLERAS\ncon puré de patata trufado\n\x0c', 'HELADO DE YOGUR Y MANGO\n\x0c', '\x0c', 'MINIPIZZA IBÉRICA\ncon queso de tetilla, tomate cherry,\nrúcula, pera y jamón ibérico\n\x0c', '8,5\n\x0c', '4,9\n\x0c', 'MEGACOOKIE\nrecien horneada, con helado de\nde vainilla y salsa de chocolate\n\x0c', '9,5\n\x0c', 'HUEVOS ROTOS\ncon foie y aceite de trufa blanca\n\x0c', 'TATAKI DE ATÚN\nrebozado en sésamo, sobre cama de fideos\nde arroz, alga wakame y germinados\n\x0c', '9,5\n\x0c', '**descubre nuestra carta de vinos, vermuts,\ncervezas, refrescos y demás bebidas en la\nsiguiente página...\n\x0c']
print(tempText)
formattedText = tpu.formatText(tempText)

translatedText = tpu.translateText(formattedText)
print(translatedText)

#ipu.get_text(spanish)
#ipu.get_text(spanish2)






    



