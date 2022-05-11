# Import required packages
import os
import shutil
from Modules import imageProcessingUtility as ipu
from Modules import textProcessingUtility as tpu
from Modules import googleImageSearchUtility as gis
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import timeit
from pprint import pprint


spanish = "../images/Spanish_menucard.jpg"
spanish2 = "../images/Spanish_menucard2.png"
spanish3 = "../images/Spanish_menucard3.jpeg"

start1 = timeit.default_timer()
#Cleaner folders
outputImages = "../outputImages"
temp_search_images = "../temp_search_images"
try:
    shutil.rmtree(outputImages)
    os.mkdir(outputImages)
    shutil.rmtree(temp_search_images)
    os.mkdir(temp_search_images)
except OSError as e:
    print("Error:" + e.strerror)


rawText = ipu.get_text(spanish,language="spa")

#tempText_spanish = ['para comer\n\x0c', 'carnes\n\x0c', 'tapas frias\n\x0c', '10,5\n\x0c', 'BURGER CLÁSICA (2208r8) !\ncon lechuga, cebolla, tomate. queso\ncheddar y pepiniíllos\n\x0c', '6.5\n\x0c', 'Sazño A y almendritas\n\x0c', '10,5\n\x0c', '6,5\n\x0c', 'BURGER MANOLETE (220gr8)\ncon jamón, queso manchego, cebolla,\nsalmorejo y lechuga\n\x0c', 'HUMMUS\ncon pan árabe\n\x0c', '75\n\x0c', 'MOUSSE DE FOIE (MI CUIT)\ncon mermelada de cerveza tostada y\nsalsa de violetas\n\x0c', '10.5\n\x0c', 'BURGER CORGONZOLA (220gr8)\ncon crema de queso gorgonzola,\ncebolla caramelízada y nueces\n\x0c', '8,5\n\x0c', "ENSALADA SIFONERA\nlochuguitas, jáminas de calabacin,\nCR 's, 541 negra, tomate seco\nsicrES de trufa blanca y\n\x0c", '10,5\n\x0c', 'SECRETO IBÉRICO\ncon espuma de euinness y regaliz,\ny patatas a la vtaíniila\n\x0c', '13,5\n\x0c', '8,5\n\x0c', 'ENSALADA CAPRESE\ncon tres tomates distintos, mozzarella\ny aceite de albahaca\n\x0c', 'LOMO DE TERNERA BRASEADO\ncon chimichurri y sus patatítas\n\x0c', '9,5\n\x0c', 'CARPACCIO DE PEZ MANTEQUILLA\ncon sal rosa, eneldo y helado de wasabi\n\x0c', 'woks\n\x0c', 'todos nuestros woks se sirven con noodles de\narroz, calabacín, zanahoria, pimiento rojo y\nverde, cebolla, sésamo, champiñón y nuestras\nsalsas secretas.\n\x0c', 'tapas calientes\n\x0c', '4,9\n\x0c', 'UNA DE BRAVAS\ncon la receta de mi madre. Puedes\npedirlas extrapicantes\n\x0c', '\x0c', 'VEGETAL\n\x0c', '5,9\n\x0c', 'GYOZAS JAPONESAS\nempanadillas orientales de pollo\ny verduras con salsa de soja\n\x0c', '\x0c', 'CON GAMBAS\n\x0c', '\x0c', 'CON POLLO\n\x0c', '9,9\n\x0c', 'CROQUETAS SIFONERAS\nlas hacemos de cecína, de gambón o\nvegetales con gorgonzola.\n\x0c', '\x0c', 'CON TERNERA\n\x0c', '6,5\n\x0c', 'postres\n\x0c', 'PROVOLETA AL HORNO\nqueso provolone horneado y\nrelleno de confíitura de tomate\n\x0c', '\x0c', 'TARTA DE QUESO\ncon arándanos o con dulce de leche\n\x0c', 'QUESADILLAS A LA ESPAÑOLA\ncon morcilla de burgos, queso\nidiazábal, manzana, miel y canela\n\x0c', '7,5\n\x0c', '\x0c', 'SUPER TORRIJA CASERA\ncon helado de leche merengada\n\x0c', '\x0c', 'PAN BAO DE RABO DE TORO\ncon rúcula, cebolla morada y\nmayonesa de Kinchee (Suas\n\x0c', 'TIRAMISÚ\n\x0c', '\x0c', 'COULANT DE CHOCOLATE\ncon salsa de chocolate blanco\n\x0c', '\x0c', '\x0c', 'DIM SUM DE CARRILLERAS\ncon puré de patata trufado\n\x0c', 'HELADO DE YOGUR Y MANGO\n\x0c', '\x0c', 'MINIPIZZA IBÉRICA\ncon queso de tetilla, tomate cherry,\nrúcula, pera y jamón ibérico\n\x0c', '8,5\n\x0c', '4,9\n\x0c', 'MEGACOOKIE\nrecien horneada, con helado de\nde vainilla y salsa de chocolate\n\x0c', '9,5\n\x0c', 'HUEVOS ROTOS\ncon foie y aceite de trufa blanca\n\x0c', 'TATAKI DE ATÚN\nrebozado en sésamo, sobre cama de fideos\nde arroz, alga wakame y germinados\n\x0c', '9,5\n\x0c', '**descubre nuestra carta de vinos, vermuts,\ncervezas, refrescos y demás bebidas en la\nsiguiente página...\n\x0c']
#tempText_spanish2 = ['Plotos Ádrede\n\x0c', 'Ensalada de “Tomate y Ventresca\n\x0c', ',00€\n\x0c', 'Vaso de Gazpacho (verano)\n\x0c', '500€\n\x0c', 'Ensaladila Rusa\n\x0c', 'AD0E\n\x0c', 'Anchoas de Laredo\n\x0c', '400€\n\x0c', 'Salmorejo\n\x0c', 'A00€\n\x0c', 'Puntas de Espárragos con Melva\n\x0c', '\x0c', 'Croquetas de Jamón y Huevo\n\x0c', '200€\n\x0c', 'Morcilla Frita con Pimientos\n\x0c', '\x0c', 'Pastel de Puerros y Queso\n\x0c', 'ADOE\n\x0c', 'Rollitos Vieinamitas\n\x0c', '100€\n\x0c', 'Habitas con Jamón\n\x0c', '400€\n\x0c', 'Provolone al Horno a la Putanesca\n\x0c', '12,00€\n\x0c', 'Alcachofas Fritas con Muselina de “Trufa\n\x0c', '12.00€\n\x0c', 'Butifarra Fresca al Jerez\n\x0c', '\x0c', 'Salmón al Horno\n\x0c', 'l6.00€\n\x0c', 'Salmón Marinado con Wokame\n\x0c', '\x0c', 'Secreto al Jerez\n\x0c', '\x0c', 'Carrillera al Porto\n\x0c', '\x0c', 'Codilo Asado y su Salsa\n\x0c', '\x0c']
#tempText_spanish3 = ['\x0c', 'CÓCTEL DE BIENVENIDA\n\x0c', 'Jamón Ibérico corte cuchillo\n\x0c', 'Buffet de quesos artesanos\n\x0c', 'Chupito de salmorejo y crujiente de jamón\nBombón de foie con crujiente de almendras\n\x0c', 'ENTRANTES\n\x0c', 'Copa de pulpo sobre puré de patotas y pimentón\n\x0c', 'Tortar de atún y oguacate con mayonesa de soja\nEnsalada de tomote ref con huevo y mojema y caviar\n\x0c', '\x0c', 'Sorbete de mojito\n\x0c', 'PLATO PRINCIPAL\n\x0c', 'Bacalao con salsa de trufa y tirmbuzones de calabacín\n\x0c', 'Pluma ibérico confitada con romero y petstes al pimentón\n\x0c', 'POSTRE\n\x0c', 'Tarta nupcial\n\x0c', 'Café, infusiones y licores en mesa\n\x0c', 'BODEGA\n\x0c', 'Vino tinto de Bodega\n\x0c', 'Vino blanco de Bodega\n\x0c', 'Cerveza, Refrescos y agua mineral\n\x0c', 'Sidra y cavo\n\x0c']
print("-----------------------------------------------------")
print("ORIGINAL TEXT!")
pprint(rawText)


print("-----------------------------------------------------")
formattedText = tpu.formatText(rawText)
print("FORMATTED TEXT!")
pprint(formattedText)


#Downloads the images
start = timeit.default_timer()
with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
    res = ex.map(gis.downloadImages,[i[0] for i in formattedText],range(len(formattedText)))
stop = timeit.default_timer()
print('Time with multi process: ', stop - start)

#Below is for measuring the download speed without multiprocessing.
''' start = timeit.default_timer()
for index, text in enumerate(formattedText):
    gis.downloadImages(text[0],index)
stop = timeit.default_timer()
print('Time without multi process: ', stop - start)  '''


print("-----------------------------------------------------")
translatedText = tpu.translateText(formattedText,"es","da")
print("TRANSLATED TEXT!")
pprint(translatedText)
stop1 = timeit.default_timer()
print('Time with multi process total: ', stop1 - start1)









    



