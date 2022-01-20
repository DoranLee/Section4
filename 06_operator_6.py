'''
    시퀸스 연산자 : 리스트, 튜플, 문자열 등에서 서로 연결할 때 사용하는 연산자
'''
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2  #두 리스트를 합치는 연산
print(lst3)
print(lst2+lst1)

str1 = 'Hello'
str2 = 'World'
print(str1+str2)

#in, not in
print(10 in lst3)     # lst3에 10이 있는지?
print(2 not in lst3)  # lst3에 2가 없는지?
print('e' in str1)
print('x' not in str1)

#삼항 연산자 : 조건식의 결과에 따라 True이면 나타낼 식, False이면 나타낼 식을 표현
# True일때 값 ~ 조건식 ~ 거짓일때 값
n = 9
msg = '짝수' if n % 2 == 0 else '홀수'
print(msg)

#반복 연산자
print('a'*3)
print('a'*4)
print('a'*5)