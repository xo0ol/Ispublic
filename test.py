import pandas as pd

x = pd.read_csv(r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\통계데이터과학과\과제물\2023-2\파이썬과R_강의자료\score.csv',
                header=0, index_col='id')
# print(x.loc[13001])
print(x.iloc[0, :])

