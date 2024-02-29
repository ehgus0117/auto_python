# 크롬 드라이버를 사용하여 구글 이미지 검색 결과를 저장한다.
# 만든날짜 2024/02/29

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import os, time
import urllib.request

keyword = input('google 이미지 검색어 입력: ')
url1 = 'https://www.google.com/search?sca_esv=5b2e6e9ffdc26326&sxsrf=ACQVn0_htAYdQcw19VUE2vrtjI2RlKBo2g:1709165545509&q='
url2 = '&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiP2s7poc-EAxURslYBHZKACfQQ0pQJegQIDRAB&biw=1920&bih=953&dpr=1'
url = url1 + keyword + url2

driver = webdriver.Chrome('chromedriver.exe')
time.sleep(0.5)

driver.get(url)
time.sleep(0.5)

# 스크롤 내리기
for i in range(15):
    time.sleep(0.5)
    try:
        # 더보기 버튼 클릭
        driver.find_element_by_css_selector('#islmp > div > div > div > div > div.C5Hr4 > div.K414Oe > div.FAGjZe > input').click()
    except:
        # 스크롤 내리기
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 이미지 URL 리스트에 추가
html = driver.page_source
soup = bs(html, 'html.parser')
# 게시글 태그를 모두 찾아 imgTagLst에 저장
imgTagLst = soup.find_all('div', class_='isv-r')

# 이미지 링크를 모두 찾아 imgLinkLst에 저장
imgLinkLst = []
for tag in imgTagLst:
    try:
        imgLinkLst.append(tag.find('img')['src'])
    except:
        imgLinkLst.append(tag.find('img')['data-src'])

# 이미지를 저장할 폴더 생성
if 'py_data' not in os.listdir('C:/'):
    os.makedirs('C:/py_data/')    

fDir = 'C:/py_data/'
fNames = os.listdir(fDir)

dirName = keyword + '0'
cnt = 0

while 1:
    if dirName not in fNames:
        os.makedirs(fDir + dirName)
        break
    cnt += 1
    dirName = keyword + str(cnt)
print(f'폴더 {dirName}이 생성되었습니다.')
        
# 이미지 저장
imgCnt = 0
for imgURL in tqdm(imgLinkLst, desc = '저장중...'):
    tempFname = fDir + dirName + '/' + keyword + str(imgCnt) + '.jpg'
    urllib.request.urlretrieve(imgURL, tempFname)
    imgCnt += 1

driver.close()