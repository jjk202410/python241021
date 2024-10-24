from openpyxl import Workbook

# 워크북 생성 및 워크시트 선택
wb = Workbook()
ws = wb.active
ws.title = "News Headlines"

# 헤더 추가
ws.append(["No.", "Headline"])

# 크롤링된 기사 제목을 엑셀에 추가
for i, headline in enumerate(headline, 1):
    ws.append([i, headline.get_text()])

# 엑셀 파일로 저장
wb.save("results.xlsx")
