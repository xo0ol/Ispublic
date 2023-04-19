import pyautogui
import time
import timeit
import math
from datetime import datetime
from datetime import timedelta

p = pyautogui
start_time = timeit.default_timer()
start_now = datetime.now()



# Ctrl + c : 강제종료

#---------------------
# 이것만 수정
worktime_min = 45
timesleep_min = 4
#---------------------

predict_endtime = start_now + timedelta(minutes=worktime_min)
print('『작업 시작 시간 : ' +  start_now.strftime('%H:%M:%S') + '』')
print('『예상 종료 시간 : ' +  predict_endtime.strftime('%H:%M:%S') + '』')
time.sleep(0.5)
print(f'{math.trunc(worktime_min)}분 동안 {math.trunc(timesleep_min)}분에 1개씩 자동 입력을 진행합니다.\n예상 입력 개수는 ' + 
      str(math.trunc(((worktime_min)/timesleep_min))) + '개 입니다.')
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
        time.sleep(1)
        p.hotkey('ctrl','v')
        

        x += 1
        now = datetime.now().strftime('%H:%M:%S')
        next_time = datetime.now() + timedelta(minutes=timesleep_min)
        next_comment = next_time.strftime('%H:%M:%S')
        print(f'{str(x).rjust(2,"0")}개 입력 완료 [{now}]\n다음 입력 시간 [{next_comment}]\n')


terminate_time = timeit.default_timer()
running_time = terminate_time - start_time
end_now = datetime.now()
print("%f분 걸렸습니다." % math.trunc(running_time/60))
print('[작업 종료 시간 : ' +  end_now.strftime('%H:%M:%S') + ']')










