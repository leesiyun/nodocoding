#7-6 지역변수와 전역변수
#지역변수 : 함수 내에서만 사용가능 한 것, 함수가 호출 될때 만들어 졌다 함수가 호출이 끝나면 끝나는 것
#전역변수 : 모든 공간에서(프로그램 내에서) 어디서든 부를수 있는 변수

gun = 10

def checkpoint(soldiers) : #경계근무
    #gun = 20
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print(f'[함수내] 남은 총 : {gun}')
    return gun

print(f'전체 총 : {gun}')
#checkpoint(2) #2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print(f'남은 총 : {gun}')