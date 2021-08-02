import PyPDF2

import sys 

import os


# Open pdf files and rotate the page

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('rotated_page.pdf', 'wb') as rotated_file:
#         writer.write(rotated_file)
        
        
# # path = 'dummy.pdf'
# path = 'rotated_page.pdf'
# os.system(path)


###############################################

# Merge several pdf files

inputs = sys.argv[1:]   

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged_pdf_files.pdf')
        
pdf_combiner(inputs)

###############################################

# Add watermark to pdf files 

template = PyPDF2.PdfFileReader(open('merged_pdf_files.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
        

path = 'watermarked_output.pdf'
os.system(path)
