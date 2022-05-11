from fpdf import FPDF
  
  
# save FPDF() class into a 
# variable pdf
height = 25
width = 25

def createPDF(dataArr):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 12)
    
    # create a cell
    pdf.cell(0, 30, txt = "GeeksforGeeks", 
            ln = 1, align = 'L')
    
    pdf.image("../temp_search_images/1/000001.jpg", x=50, y=100, h=height, w=width)
    pdf.image("../temp_search_images/1/000003.jpg", x=50+width, y=100, h=height, w=width)

    # add another cell
    pdf.cell(0, 10, txt = "A Computer Science portal for .jdfssdfsd sdfjsdklf nldsfnsdf sdfijsdf lidjflsdf kihfsdnf kifsl fldfn dflshfkf  khdfsdflnsdfi lknsdfnsf  lksdjfj fsdfn lsdkfnld",
            ln = 2, align = 'L')
    
    # save the pdf with name .pdf
    pdf.output("GFG.pdf")

createPDF([])