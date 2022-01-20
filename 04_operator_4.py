'''
    논리연산자
        and : 양쪽의 조건식이 둘 다 True일 때, True
        or  : 양쪽의 조건식 중 하나라도 True일 때, True
        not : 오른쪽의 조건식의 결과를 반대로 뒤집는 연산(True면 False, False면 True로 바꿈)
'''
n1, n2 = 10, 7
print(n1 > 5 and n2 < 7)
print(n1 > 5 and n2 < 10)
print(n1 > 5 or n2 < 7)
print(n1 < 5 or n2 < 7)

result = n1 > 10  #False
print(not result) #True
print(not n1 > 10)
print(not (n1 > 5 and n2 < 7))

# n1이 5보다 크고 n2가 10보다 작고 n1이 n2와 다른가?
result = n1 > 5 and n2 < 10 and n1 != n2
print(result)
