# BankAccount.py

#은행의 계정을 표현한 클래스 
#무조건 public 선언만 된다.... 
class BankAccount:
    #초기화
    #클래스 내부에 이름 숨김 __
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        # \ 는 한줄로 연결한다는 뜻
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
#클래스 외부 ==> 인스턴스
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)

#외부에서 접근, 보안상 문제가 있음..
#account1.balance = 150000000
print(account1)
#print(account1.__balance)

