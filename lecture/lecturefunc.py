import re
from datetime import datetime, timedelta

# 시간표 테이블 기초 데이터 작업

def lecture_time(mylecture_list):

    # print(mylecture_list)
    # 요일별 데이터 만들기
    for item in mylecture_list:
        name = item[2] #강사명
        subject = item[3] #과목
        lect_nm = item[4] #강의명

        yoil = re.compile('[가-힣]')  # 요일
        yoil = yoil.findall(item[6])

        t1 = re.compile('[0-9][0-9]:[0-9][0-9]') #시간 첫 번째
        t1 = t1.findall(item[7])

        t2 = re.compile('[0-9][0-9]:[0-9][0-9]')  # 시간 두 번째
        t2 = t2.findall(item[8])

        #요일 갯수 만큼 강의명, 요일, 시간을 저장한다.

        min = 30
        for k in range(0,len(yoil)):

            time_1 = datetime.strptime(t1[k], "%H:%M") #시간간격을 구한다
            time_2 = datetime.strptime(t2[k], "%H:%M")  # 시간간격을 구한다
            time_interval = time_2 - time_1
            # print(time_interval)
            term = time_interval / 30
            term = str(term)
            term = int(term[3:4])

            print(name)
            print(yoil[k])
            print(term)

            if term > 0 and type(term) == int:
                for i in range(0, term):
                    if i == 0:
                        set_time = time_1
                    else:
                        set_time = time_1 + timedelta(minutes=min)
                    min = min + 30

                    print(set_time)
            min = 0



        # print(term.strftime[2:3])

        # print(time_1 + timedelta(minutes=30))

        # print(time_interval)

        # locals()['{}_data'.format(kind)] = item[4]



        # print(name)
        # print(subject)
        # print(lect_nm)
        # print(yoil)
        # print(len(yoil))
        # print(t1)
        # print(t2)


    return mylecture_list