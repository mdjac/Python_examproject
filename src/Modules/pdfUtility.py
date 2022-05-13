from fpdf import FPDF
from PIL import Image
import os, os.path
  
  
# save FPDF() class into a 
# variable pdf
height = 25
width = 25

def createPDF(dataArr):
    print(dataArr[0].get('translated'))
    pdf = FPDF()
    pdf.add_font("Arial", "", "./Modules/arial.ttf", uni=True)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin = 65.0)

    pdf.set_font("Arial", "B",size = 12, )
    
    for index, item in enumerate(dataArr):
        print(item)
        pdf.set_font("Arial", size = 15)
        pdf.cell(0,h=5, txt=item.get('original')[0] + " / "+item.get('translated')[0],ln=1)
       
        #pdf.cell(10, 30, txt = item.get('original')[0] + " / "+item.get('translated')[0], 
        #    ln = 1, align = 'L')
        if (len(item.get('original')) >1):
            pdf.set_font("Arial", size = 10)
            pdf.multi_cell(0,h=5, txt=" ".join(item.get('original')[1:]) + " / "+" ".join(item.get('translated')[1:]))
            
            
        else:
            pdf.cell(0,h=3, txt="", ln=1)
            print(pdf.get_y())
        
        dirPath = "../temp_search_images/"+str(index)+"/"
        #Loop pictures
        try:
            files =  os.listdir(dirPath)
            
            for index, f in enumerate(files):
                print(dirPath+f)
                pdf.image(dirPath+f, x=10+(width+5)*index, y=pdf.get_y(), h=height, w=width)
        except:
            pass
        
                #pdf.image(os.path(f), x=(width+5)*index, y=pdf.get_y(), h=height, w=width)
        #pdf.image("../temp_search_images/1/L2VzbmdkZ1U4Zmd3Mm5LOVYxLlc3aUFfYi5qcGc=.jpg", x=10+width+5, y=pdf.get_y(), h=height, w=width)
        pdf.ln(40)
        
    
    # save the pdf with name .pdf
    pdf.output("GFG.pdf")
    pdf.close()

