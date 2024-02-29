import PyPDF2

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

# 합치기
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)  
    pdfWriter.addPage(pageObj)

for pageNum in range(1,pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)  
    pdfWriter.addPage(pageObj)

pdf1 = open('combined.pdf', 'wb')
pdfWriter.write(pdf1)
pdf1.close()
pdf1File.close()
pdf2File.close()

# 워터마크
pdf2 = open('combined.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf2)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

for page in range(pdfReader.numPages):
    pdfReader.getPage(page).mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(pdfReader.getPage(page))

combineWater = open('combind_water.pdf', 'wb')
pdfWriter.write(combineWater)
pdf2.close()
combineWater.close()

# 암호화
pdf3 = open('combind_water.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf3)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('password')
resultPdf = open('finalPDF.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
pdf3.close()

