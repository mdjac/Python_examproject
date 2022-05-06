# Import required packages
import os
import shutil
from Modules import imageProcessingUtility as ipu



spanish = "../images/Spanish_menucard.jpeg"
spanish2 = "../images/Spanish_menucard2.png"
spanish3 = "../images/Spanish_menucard3.jpeg"

#Cleaner output images
dir_path = "../outputImages"
try:
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))


result = ipu.get_text(spanish,language="spa")
print(result)
#ipu.get_text(spanish)
#ipu.get_text(spanish2)






    



