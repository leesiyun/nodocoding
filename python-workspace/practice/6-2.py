#6-2 for
print('대기번호 : 1')
print('대기번호 : 2')
print('대기번호 : 3')
print('대기번호 : 4')

for waithing_no in [0,1,2,3,4] :
    print(f'대기번호 : {waithing_no}')

#randrange()
for waithing_no in range(1,6) : #1,2,3,4,5
    print(f'대기번호 : {waithing_no}')

starbucks = ['아이언맨', '토르', '아이엠 그루트']
for customer in starbucks : 
    print(f'{customer}, 커피가 준비되었습니다')
