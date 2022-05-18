from fpdf import FPDF
from PIL import Image
import os, os.path
from tqdm import tqdm
import config
  

height = config.pdf_settings['image_height']  
width = config.pdf_settings['image_width']  

def createPDF(dataArr):
    pdf = FPDF()
    pdf.add_font("Arial", "", "./Modules/arial.ttf", uni=True)
    pdf.add_font("Arial", style="B", fname="./Modules/arial_bold.ttf", uni=True)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin = 65.0)

    for index, item in enumerate(tqdm(dataArr)):
        pdf.set_font("Arial","B",size = config.pdf_settings['heading_size'] )
        pdf.multi_cell(0,h=5, txt=u""+item.get('original')[0] + " / "+item.get('translated')[0])
       
        if (len(item.get('original')) >1):
            pdf.set_font("Arial", size = config.pdf_settings['paragraph_size'] )
            pdf.multi_cell(0,h=5, txt=u" ".join(item.get('original')[1:]) + " / "+" ".join(item.get('translated')[1:]))
            
            
        else:
            pdf.cell(0,h=3, txt="", ln=1)
        
        dirPath = "../temp_search_images/"+str(index)+"/"
        #Loop pictures
        try:
            files =  os.listdir(dirPath)
            for index, f in enumerate(files):
                try:
                    pdf.image(dirPath+f, x=10+(width+5)*index, y=pdf.get_y(), h=height, w=width)
                except:
                    pass
                    pdf.image("./Modules/NO_IMAGE.jpg", x=10+(width+5)*index, y=pdf.get_y(), h=height, w=width)
                    
                
        except:
            pass
        pdf.ln(40)
        
    
    # save the pdf with name .pdf
    print("Saving PDF")
    pdf.output("result.pdf")
    pdf.close()

