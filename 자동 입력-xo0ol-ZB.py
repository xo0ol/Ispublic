import pyautogui
import math

import time # time.sleep() 을 위한 패키지
import timeit # 시간을 숫자단위로 측정. 시작시간-종료시간으로 작업시간을 계산
from datetime import datetime # datetime.now() 을 위한 패키지
from datetime import timedelta # 시간끼리의 연산을 위한 패키지

p = pyautogui


# 시작시간 설정
start_now = datetime.now()
start_time = timeit.default_timer()


#---------------------
# 이것만 수정

worktime_min = 110 # 몇 분동안 동작는걸 원하는지?
timesleep_min = 7 # 몇 분에 한번씩 입력을 원하는지?

#---------------------


# 작업 시작 알림
predict_endtime = start_now + timedelta(minutes=worktime_min)
print('『 작업 시작 시간 : ' +  start_now.strftime('%H:%M:%S') + ' 』')
print('『 예상 종료 시간 : ' +  predict_endtime.strftime('%H:%M:%S') + ' 』')
time.sleep(0.5)
print(f'『 {math.trunc(worktime_min)}분 동안 {math.trunc(timesleep_min)}분에 1개씩 자동 입력을 진행합니다. 』\n『 예상 입력 개수는 ' + 
      str(math.trunc(((worktime_min)/timesleep_min))) + '개 입니다. 』')
print('')


x = 0
while True:
    if datetime.now() >= start_now + timedelta(minutes=worktime_min):
        break

    else:
        time.sleep((timesleep_min*60)-2)
        p.hotkey('ctrl','c')
        time.sleep(1)
        p.press('down')
        # p.press('up')
        time.sleep(1)
        p.hotkey('ctrl','v')
        
        x += 1
        now = datetime.now().strftime('%H:%M:%S')
        next_time = datetime.now() + timedelta(minutes=timesleep_min)
        next_comment = next_time.strftime('%H:%M:%S')
        print(f'{str(x).rjust(2,"0")}개 입력 완료 [{now}]\n다음 입력 시간 [{next_comment}]\n')



# 작업 종료 알림
end_now_str = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
finished_time = timeit.default_timer()
running_time = math.trunc(finished_time - start_time)


if running_time % 60 == running_time:
    x_time = f'00:{str(running_time).rjust(2,"0")}'
else:
    x1 = math.trunc(running_time / 60)
    x2 = running_time & 60
    x_time = f'{str(x1).rjust(2,"0")}:{str(x2).rjust(2,"0")}'


print(f'『 {(x_time)} 소요되었습니다. 』')
print(f"『 {end_now_str} 작업을 종료합니다. 』")