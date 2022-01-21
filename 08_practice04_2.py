sec = int(input('초를 입력하세요 >> '))
h = sec // 3600
sec %= 3600
m = sec // 60
sec %= 60
# like 모래 필터링
print('{}시간 {}분 {}초'.format(h, m, sec))
print(f'{h}시간 {m}분 {sec}초')