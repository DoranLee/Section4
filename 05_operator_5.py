'''
    비트연산자
        &(and, 둘 모두가 1이면 1)
        |(or, 둘 중 하나가 1이면 1)
        ^(xor, 양쪽의 숫자가 달라야 1)
        ~(not, 0과 1을 바꿀때)
        >> <<
'''

n1, n2 = 10, 7
'''
000000000000001010  -> n1 = 10
000000000000000111  -> n2 = 7
-------------------
& 0000000000000010  -> 2
| 0000000000001111  -> 15
^ 0000000000001101  -> 13
'''
print(n1 & n2)
print('and : ', n1&n2)
print('or : ', n1|n2)
print('xor : ', n1^n2)
print('not : ', ~n1)

n3 = 1
print(n3 << 3)
'''
n3 0000000001
<< 0000001000  <- <<3 = X2X2X2
'''
n4 = 256
print(n4>>1)
print(n4>>2)
print(n4>>3)  # >>3 = /2/2/2

n5=-11
print(n5>>2)  # 부호비트는 밀리지 않음(그대로)

#특정분야 아니면 쓸일이 별로~?