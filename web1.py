# web1.py
# 웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

#웹페이지를 로딩
page = open("chap09_test.html", "rt", encoding="utf-8").read()

# html 파서 : "상수값을 지정"
soup = BeautifulSoup(page, "html.parser")

# 원하는 부분 추출
#print(soup.prettify())

# <p> 태그 전부 출력
# print(soup.find_all("p"))

# <p> 태그 중에서 첫번째 데이터만 출력
# print(soup.find("p"))

# 조건검색 : <p class="outer-text">
# print(soup.find_all("p", class_="outer-text"))

# attr 속성검색 : attributes 속성검색
print(soup.find_all("p", attrs={"class":"outer-text"}))

# 태그 내부 문자열 출력 : .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)    

# id로 검색
print(soup.find_all(id="first"))








