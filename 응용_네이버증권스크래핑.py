import requests
from bs4 import BeautifulSoup
import os
import openpyxl


url1 = 'https://finance.naver.com/item/main.naver?code='
codeLst = []
stock_name = []
date = []
price = []
print('5가지를 입력하세요')
for i in range(5):
    
    stock_code = input('주식코드 입력(6자리): ')
    codeLst.append(stock_code)
    url = url1 + str(codeLst[i])
    html = requests.get(url) 
    soup = BeautifulSoup(html.text, 'html.parser')

    ulTag = soup.find('div', class_='wrap_company')
    dlTag = ulTag.find('h2')
    stock_name.append(dlTag.text)
    
    ulTag = soup.find('p', class_='no_today')
    dlTag = ulTag.find('span')
    num = str.replace(dlTag.text, ",","")
    type(int(num)) # 정수로 변환
    price.append(num)

    ulTag = soup.find('em', class_='date')
    date.append(ulTag.text)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.column_dimensions['A'].width = 30
sheet.column_dimensions['B'].width = 30
sheet.column_dimensions['C'].width = 30

sheet['A1'] = '날짜'
sheet['B1'] = '이름'
sheet['C1'] = '가격'

for i in range(5):
    sheet.append([date[i], stock_name[i], price[i]])
wb.save('stock.xlsx')
print('엑셀 생성 완료')



