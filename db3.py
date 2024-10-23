import sqlite3
import random

class FoodDrinkDatabase:
    def __init__(self, db_name='food_drink.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products
        (id INTEGER PRIMARY KEY,
         name TEXT NOT NULL,
         price REAL NOT NULL)
        ''')
        self.conn.commit()

    def insert(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def update(self, id, name=None, price=None):
        if name and price:
            self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, id))
        elif name:
            self.cursor.execute('UPDATE products SET name = ? WHERE id = ?', (name, id))
        elif price:
            self.cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        self.conn.commit()

    def select_all(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def select_by_id(self, id):
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

# 샘플 데이터 생성 함수
def generate_sample_data():
    foods = ['피자', '햄버거', '파스타', '샐러드', '스테이크', '샌드위치', '타코', '초밥', '라면', '김치찌개']
    drinks = ['콜라', '사이다', '주스', '커피', '차', '맥주', '와인', '소주', '위스키', '칵테일']
    
    products = []
    for i in range(50):
        food_name = f"{random.choice(foods)} {i+1}"
        food_price = round(random.uniform(5000, 30000), -2)  # 5000원에서 30000원 사이, 100원 단위로 반올림
        products.append((food_name, food_price))

    for i in range(50):
        drink_name = f"{random.choice(drinks)} {i+1}"
        drink_price = round(random.uniform(1000, 10000), -2)  # 1000원에서 10000원 사이, 100원 단위로 반올림
        products.append((drink_name, drink_price))

    return products

# 데이터베이스 사용 예시
if __name__ == "__main__":
    db = FoodDrinkDatabase()

    # 샘플 데이터 생성 및 삽입
    sample_data = generate_sample_data()
    for name, price in sample_data:
        db.insert(name, price)

    # 전체 데이터 조회
    all_products = db.select_all()
    print("전체 제품 목록:")
    for product in all_products:
        print(product)

    # ID로 특정 제품 조회
    product_id = 5
    product = db.select_by_id(product_id)
    print(f"\nID {product_id}의 제품 정보:", product)

    # 제품 정보 업데이트
    db.update(product_id, name="업데이트된 제품명", price=15000)
    updated_product = db.select_by_id(product_id)
    print(f"\n업데이트된 제품 정보:", updated_product)

    # 제품 삭제
    db.delete(product_id)
    deleted_product = db.select_by_id(product_id)
    print(f"\n삭제된 제품 조회 결과:", deleted_product)

    db.close()