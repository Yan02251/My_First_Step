import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lst_all = lst50 + lst100
print(len(lst_all))


#순위 변수명 rank
#제목 변수명 title
#가수 변수명 singer
#앨범 변수명 album
