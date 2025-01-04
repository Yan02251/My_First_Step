from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

#클래스, 아이디를 css_selector를 이용해서 원하는 값을 가져오기 위한 패키지
from selenium.webdriver.common.by import By
#키보드의 입력 형태를 코드로 작성하기 위해 사용하는 패키지
from selenium.webdriver.common.keys import Keys

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

options_ = Options() #클래스 인스턴스화
options_.add_argument(f"User_Agent={header_user}") #유저 정보 넣기
options_.add_experimental_option("detach", True) #브라우저 자동 종료 방지
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(options=options_)

url = "https://kream.co.kr"
driver.get(url)

#돋보기 누르기
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()