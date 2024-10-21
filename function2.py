#약간 더 복잡한 함수
#합집합 함수
def union(*ar):
    #지역변수
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result
#호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

#람다함수 정의
g = lambda x,y:x*y
print(g(3,4))
print( (lambda x:x*x)(3))

print( globals())
print( dir())


