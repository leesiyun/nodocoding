#8-1 표준입출력
print('python', 'Java')
print('python' + 'Java')
print('python', 'Java', sep=',')
print('python', 'Java', 'Javascript', sep=' vs ')

print('python', 'Java', sep=',', end='?')
print('무엇이 더 재밌을까요?')

print('python', 'Java', sep=',')
print('무엇이 더 재밌을까요?')

import sys
print('python', 'Java', file=sys.stdout)
print('python', 'Java', file=sys.stderr)

#시험성적
scores = {'수학' : 0, '영어' : 50, '코딩' : 100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':')

##001, 002, 003, ...
for num in range(1, 21) : 
    print('대기번호 : ' + str(num).zfill(3))

answer = input('아무 값이나 입력하세요 : ')
#answer = 10
print(type(answer))
print(f'입력하신 값은 {answer} 입니다.')