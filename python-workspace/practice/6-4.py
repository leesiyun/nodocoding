#6-4 continue와 break
no_book = [7] #책을 깜빡했음
absent = [2,5] #결석
for student in range(1, 11) : #1,2,3,4,5,6,7,8,9,10
    if student in absent :
        continue
    elif student in no_book : 
        print(f'오늘 수업 여기까지. {student}는 교무실로 따라와')
        break
    print(f'{student}, 책을 읽어봐')