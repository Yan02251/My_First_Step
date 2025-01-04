from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요: ")
url = base_url + keyword

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

options_ = Options() #클래스 인스턴스화
options_.add_argument(f"User_Agent={header_user}") #유저 정보 넣기
options_.add_experimental_option("detach", True) #브라우저 자동 종료 방지
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(options=options_)
driver.get(url)
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap")

for i in results: 
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")["href"]
    writer = i.select_one(".name").text
    dsc = i.select_one(".dsc_link").text
    print(f"제목 : {title}")
    print(f"링크 : {link}")
    print(f"작성자 : {writer}")
    print(f"글요약 : {dsc}")
    print("--------------")
driver.quit()
