# DemoRe.py
# 정규포현식 사용
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

result2 = re.match("[0-9]*th", "  35th")
print(result)
print(result.group())



def check_email(email):
    # 이메일 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.search 함수를 사용하여 이메일 체크
    if re.search(pattern, email):
        return True
    else:
        return False

# 테스트할 이메일 샘플
email_samples = [
    "user@example.com",                # 유효한 기본 이메일
    "user.name@example.co.kr",         # 유효한 이메일 (복합 도메인)
    "user+tag@example.com",            # 유효한 이메일 (+ 기호 포함)
    "123@example.com",                 # 유효한 이메일 (숫자로 시작)
    "user@subdomain.example.com",      # 유효한 이메일 (서브도메인 포함)
    "user-name@example.com",           # 유효한 이메일 (하이픈 포함)
    "user@example.photography",        # 유효한 이메일 (긴 최상위 도메인)
    "invalid.email@com",               # 유효하지 않은 이메일 (잘못된 도메인)
    "user@.com",                       # 유효하지 않은 이메일 (도메인 이름 누락)
    "user@example..com"                # 유효하지 않은 이메일 (연속된 점)
]

# 이메일 샘플 테스트
for email in email_samples:
    if check_email(email):
        print(f"'{email}' 은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"'{email}' 은(는) 유효하지 않은 이메일 주소입니다.")

