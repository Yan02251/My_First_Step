import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# lst50과 lst100에서 차트 데이터를 선택
lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lst_all = lst50 + lst100
print(f" TOP {len(lst_all)} 리스트")

# 순위, 제목, 가수, 앨범을 출력
for rank, i in enumerate(lst_all, start=1):  # 순위를 1부터 시작
    try:
        title = i.select_one(".ellipsis.rank01").text # 제목
        singer = i.select_one(".ellipsis.rank02").text # 가수
        album = i.select_one(".ellipsis.rank03").text  # 앨범
    except AttributeError:
        # 예외 처리: 일부 항목이 누락될 수 있으므로
        continue

    print(f"순위: {rank}")
    print(f"제목: {title}")
    print(f"가수: {singer}")
    print(f"앨범: {album}")
    print("--------------")