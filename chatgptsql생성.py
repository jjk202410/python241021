import sqlite3
import random

# 제품 관리 클래스 정의
class ProductDatabase:
    def __init__(self, db_name="products.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    # 테이블 생성
    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            ''')

    # 제품 추가 (INSERT)
    def insert_product(self, product_name, price):
        with self.conn:
            self.conn.execute('''
                INSERT INTO products (product_name, price)
                VALUES (?, ?)
            ''', (product_name, price))

    # 제품 수정 (UPDATE)
    def update_product(self, product_id, new_name=None, new_price=None):
        if new_name is not None:
            with self.conn:
                self.conn.execute('''
                    UPDATE products
                    SET product_name = ?
                    WHERE product_id = ?
                ''', (new_name, product_id))
        
        if new_price is not None:
            with self.conn:
                self.conn.execute('''
                    UPDATE products
                    SET price = ?
                    WHERE product_id = ?
                ''', (new_price, product_id))

    # 제품 삭제 (DELETE)
    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute('''
                DELETE FROM products
                WHERE product_id = ?
            ''', (product_id,))

    # 제품 조회 (SELECT)
    def select_products(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()

    # 샘플 데이터 생성
    def generate_sample_data(self, num_samples=100):
        sample_names = ["TV", "Smartphone", "Laptop", "Tablet", "Camera", "Headphones", "Smartwatch", "Monitor", "Keyboard", "Mouse"]
        for _ in range(num_samples):
            name = random.choice(sample_names)
            price = round(random.uniform(50, 3000), 2)  # 50 ~ 3000 사이의 랜덤 가격
            self.insert_product(name, price)

    # 클래스 소멸 시 커넥션 종료
    def __del__(self):
        self.conn.close()

# 사용 예시
if __name__ == "__main__":
    # 데이터베이스 연결 및 초기화
    db = ProductDatabase()

    # 샘플 데이터 100개 추가
    db.generate_sample_data(100)

    # 데이터 조회
    products = db.select_products()
    for product in products:
        print(product)

    # 데이터 업데이트 예시
    db.update_product(product_id=1, new_name="Updated TV", new_price=1999.99)

    # 데이터 삭제 예시
    db.delete_product(product_id=2)

    # 변경된 데이터 조회
    updated_products = db.select_products()
    for product in updated_products:
        print(product)
