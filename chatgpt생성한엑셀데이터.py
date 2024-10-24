import sqlite3
import openpyxl
import random

# SQLite 데이터베이스 연결
conn = sqlite3.connect('MyProd.db')
cursor = conn.cursor()

# 제품 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS 제품
                  (제품ID TEXT PRIMARY KEY, 제품명 TEXT, 수량 INTEGER, 가격 INTEGER)''')

# 제품명 리스트 생성
제품명_리스트 = ['스마트폰', '노트북', '태블릿', '스마트워치', '이어폰', '블루투스 스피커', 
             '게이밍 마우스', '키보드', '모니터', '프린터']

# 100개의 데이터 생성 및 데이터베이스에 삽입
for i in range(1, 101):
    제품ID = f'P{i:03d}'
    제품명 = random.choice(제품명_리스트)
    수량 = random.randint(1, 100)
    가격 = random.randint(10000, 2000000)
    
    cursor.execute("INSERT INTO 제품 (제품ID, 제품명, 수량, 가격) VALUES (?, ?, ?, ?)",
                   (제품ID, 제품명, 수량, 가격))

# 변경사항 저장
conn.commit()

# 데이터베이스에서 데이터 조회
cursor.execute("SELECT * FROM 제품")
rows = cursor.fetchall()

# 새 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "전자제품 판매 데이터"

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 데이터베이스의 데이터를 엑셀에 추가
for row in rows:
    ws.append(row)

# 엑셀 파일 저장
wb.save("products.xlsx")

# 데이터베이스 연결 종료
conn.close()

print("MyProd.db 파일과 products.xlsx 파일이 생성되었습니다.")