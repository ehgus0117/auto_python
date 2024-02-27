# 여러 PDF에서 선택한 페이지를 결합하기
import PyPDF2, os

# 모든 PDF 파일의 이름 얻기
pdfFiles = []
for fileName in os.listdir('.'):
    if fileName.startswith('meetingminutes'):  #fileName[:-4] == '.pdf'
        pdfFiles.append(fileName)

# fileName 리스트에 파일 이름을 정렬
pdfFiles.sort(key = str.lower)
print(f'정렬 결과: {pdfFiles}')

# 결과 PDF를 위한 PdfFileWriter 객체를 생성
pdfWriter = PyPDF2.PdfFileWriter()

# 모든 PDF 파일에 대해서 반복한다.
for fileName in pdfFiles:
    pdfFileObj = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # 모든 페이지에 대해 반복하고(첫 페이지 제외) 추가한다.
    for pageNum in range (1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        
#최종 결과 저장
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
