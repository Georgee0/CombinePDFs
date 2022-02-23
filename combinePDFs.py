# python3
# combinePDFs.py : Combine all PDFs in the working dirctory and add them to a single PDF

import PyPDF2, os

# Get all PDFs filenames
print('Getting PDF Filenames.............')
PdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        PdfFiles.append(filename)
PdfFiles.sort(key=str.lower)        

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through the PDFs.
for filename in PdfFiles:
    pdfObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObj)
    
# Loop through all pages of the PDfs eep the first one add thm    
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        print('Adding PDFs............')
 # Save resulting PDfs to a file.
pdfOutput = open('allminutes.pdf', 'wb')       
pdfWriter.write(pdfOutput)
pdfOutput.close()
print('Saving............')
print('Done!')