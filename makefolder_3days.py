import os # 폴더 생성 패키지
from datetime import datetime # datetime.now() 을 위한 패키지
from datetime import timedelta # 어제 날짜를 가져오기 위한 패키지
import shutil # 파일을 옮겨주는 패키지



#=============================================
# 날짜를 텍스트로 받아오기
day = 1
yesterday_YMD = []
for x in range(day):
    yesterday_YMD.append((datetime.today()-timedelta(x+1)).strftime("%y%m%d"))

# print(yesterday_YMD)
#=============================================




for j in yesterday_YMD:

    #=============================================
    # 기존 경로와 이동 경로 설정
    src = r'C:\POS'
    dst = r'C:\POS\{}'.format(j)
    # print(src, dst)
    #=============================================


    #=============================================
    # 파일명 설정
    filename = [f"CP_SA_{j}",
                f"CP_WIST_{j}",
                f"CP_RV_{j}",
                f"EM_SA_{j}",
                f"EM_ST_{j}",
                f"EM_WI_{j}"]
    # print(filename)
    #=============================================


    #=============================================
    # 어제 날짜의 폴더 생성
    try:

        os.mkdir(f"C:\POS\{j}")
        print(f"completed creating the folder [{j}]")

    except:

        print("ERROR : 파일이 이미 있으므로 만들 수 없습니다.")
    #=============================================


    #=============================================
    # 파일 옮기기
    file_count = 0
    for x in filename:
        try:
            shutil.move(f"{src}\{x}.csv", f"{dst}\{x}.csv")
            print(f"파일 이동 성공 : {x}")
            file_count +=1
        except:
            next

    print(f"[{j}] 폴더에 총 [{file_count}] 개의 파일을 이동하였습니다.")
    #=============================================