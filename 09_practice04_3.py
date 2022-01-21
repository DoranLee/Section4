emp_n = int(input('사번을 입력하세요(4자리) >>'))
emp_n %= 10
msg = '오전' if emp_n >=5 else '오후'
print('근무시간은 {}입니다.'.format(msg))

msg2 = '아침' if emp_n%10 >=5 else '오후'
print('근무시간은 {}입니다.'.format(msg2))
print(emp_n%10)
