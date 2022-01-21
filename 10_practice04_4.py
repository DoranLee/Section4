print('한 박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
rm = int(input('라면 개수 >> '))
box = rm//20
box += 1 if rm % 20 != 0 else 0
print('라면 {}개를 담으려면 {}박스가 필요합니다.'.format(rm, box))
print(f'라면 {rm}개를 담으려면 {box}박스가 필요합니다.')

box2 = rm//20
box3 = 0 if rm % 20 == 0 else 1
print('{}개'.format(box2+box3))