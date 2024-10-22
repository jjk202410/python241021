class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_classes():
    # Person 객체 생성 및 테스트
    p1 = Person(1, "John")
    p1.printInfo()  # ID: 1, Name: John

    p2 = Person(2, "Alice")
    p2.printInfo()  # ID: 2, Name: Alice

    # Manager 객체 생성 및 테스트
    m1 = Manager(3, "Bob", "Project Manager")
    m1.printInfo()  # ID: 3, Name: Bob, Title: Project Manager

    m2 = Manager(4, "Charlie", "HR Manager")
    m2.printInfo()  # ID: 4, Name: Charlie, Title: HR Manager

    # Employee 객체 생성 및 테스트
    e1 = Employee(5, "David", "Python")
    e1.printInfo()  # ID: 5, Name: David, Skill: Python

    e2 = Employee(6, "Eve", "JavaScript")
    e2.printInfo()  # ID: 6, Name: Eve, Skill: JavaScript

    # 추가 테스트: 객체를 리스트에 넣고 반복 처리
    persons = [p1, p2, m1, m2, e1, e2]
    for person in persons:
        person.printInfo()

# 10개 테스트 실행
test_classes()
