from bs4 import BeautifulSoup
import requests

# 네이버 검색 결과 페이지 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 헤더 생성
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# GET 요청을 통해 HTML 코드 가져오기
response = requests.get(url, headers=headers)

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 기사 제목 선택 (CSS 선택자 수정 필요)
headlines = soup.select('.news_tit')

# 기사 제목 출력
for i, headline in enumerate(headlines, 1):
    print(f"{i}. {headline.get_text()}")
