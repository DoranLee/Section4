s = int(input('국어점수 >> '))
s += int(input('수학점수 >> '))
s += int(input('영어점수 >> '))
s /= 3  #평균
msg = '합격' if s >= 80 else '불합격'
print('평균 {}점으로 {}입니다.'.format(s,msg))

print('----')
s1 = int(input('국어점수 >'))
s2 = int(input('수학점수 >'))
s3 = int(input('영어점수 >'))
msg = '합격' if (s1+s2+s3)/3 >= 80 else '불합격'
print(f'평균 {(s1+s2+s3)/3}점으로 {msg}입니다.')