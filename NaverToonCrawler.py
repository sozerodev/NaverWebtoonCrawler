# ================================================================================
# "https://comic.naver.com/webtoon/finish.nhn?view=list&order=Update"에서의 선택자

# 컨테이너 : tbody > tr
# 평점 : div.rating_type strong    /   div.rating_type strong
# 작가이름 : tr.first td a  /   td:nth-of-type(3) a
# 제목 : td.subject strong    /   td:nth-of-type(1) a

# ================================================================================
# 상세 페이지의 선택자

# 장르 : p.detail_info span.genre
# 스토리요약 : div.detail p
# =================================================================================
import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "평점", "작가", "장르", "스토리요약"])

raw = requests.get("https://comic.naver.com/webtoon/finish.nhn?view=list&order=Update",
                   headers = {"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')
webtoons = html.select("tbody > tr")

for webtoon in webtoons:
    title = webtoon.select_one("td:nth-of-type(1) a")
    url = title.attrs["href"]

    score = webtoon.select_one("div.rating_type > strong").text
    author = webtoon.select_one("td:nth-of-type(3) a").text


    each_raw = requests.get("https://comic.naver.com" + url,
                            headers = {"User-Agent" : "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    genre = each_html.select_one("p.detail_info span.genre").text
    storysum = each_html.select_one("div.detail p").text


    print("제목 :"+title.text)
    print("-"*20)
    print("평점 :"+ score)
    print("작가 :"+ author)
    print("장르 :"+genre)
    print("요약 :"+storysum)
    print("="*50)

    sheet.append([title.text, score, author, genre, storysum])

wb.save("NaverToonInfo.xlsx")
