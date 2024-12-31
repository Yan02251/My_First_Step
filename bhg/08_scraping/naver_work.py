import requests
from bs4 import BeautifulSoup

# URL 및 검색어 설정
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요: ")
url = base_url + keyword

# HTTP 요청
try:
    req = requests.get(url)
    req.raise_for_status()  # HTTP 오류 확인
except requests.exceptions.RequestException as e:
    print(f"HTTP 요청 실패: {e}")
    exit()

# HTML 파싱
html = req.text
soup = BeautifulSoup(html, "html.parser")

# 결과 추출
results = soup.select(".view_wrap")  # 검색 결과의 래퍼 클래스
if not results:
    print("검색 결과가 없습니다. HTML 구조를 확인하세요.")
    exit()

# 데이터 출력
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