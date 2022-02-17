import re
from datetime import datetime, timedelta

# 시간표 테이블 기초 데이터 작업

def lecture_time(mylecture_list):

    info = {}
    teacher = {}

    # print(mylecture_list)
    # 요일별 데이터 만들기

    for item in mylecture_list:
        name = item[2] #강사명
        subject = item[3] #과목
        lect_nm = item[4] #강의명

        yoil = re.compile('[가-힣]')  # 요일
        yoil = yoil.findall(item[6])

        grade = re.compile('[가-힣]*[1-9]') # 학년
        grade = grade.findall(item[5])

        # print(grade)

        t1 = re.compile('[0-9][0-9]:[0-9][0-9]') #시간 첫 번째
        t1 = t1.findall(item[7])

        t2 = re.compile('[0-9][0-9]:[0-9][0-9]')  # 시간 두 번째
        t2 = t2.findall(item[8])

        #요일 갯수 만큼 강의명, 요일, 시간을 저장한다.

        for k in range(0, len(yoil)):
            mins = 30
            time_1 = datetime.strptime(t1[k], "%H:%M") #시간간격을 구한다
            time_2 = datetime.strptime(t2[k], "%H:%M")  # 시간간격을 구한다
            time_interval = time_2 - time_1
            # print(time_interval)
            term = time_interval / 30
            term = str(term)
            term = int(term[3:4])

            # print(name)
            # print(yoil[k])
            # print(term)

            if term > 0 and type(term) == int:
                for i in range(0, term):
                    if i == 0:
                        set_time = time_1
                    else:
                        set_time = time_1 + timedelta(minutes=mins)
                        mins = mins + 30

                    set_time = str(set_time)
                    set_time = set_time[11:16]
                    # print(set_time)
                    # print(mins)
                    info_time = str(time_1)
                    info_time = info_time[11:16]
                    info[f"{yoil[k]}_{name}_{subject}_{set_time}"] = f"{grade}_{lect_nm}_{info_time}" #강의정보

                    #요일별 강사명
                    teacher[f'{name}_{yoil[k]}'] = f'{yoil[k]}'




    # print(info)
    print(teacher)

        # 월_하명래_국어_0830 = '고1\n수능국어'
        # print(월_하명래_국어_0830)

        # locals()['{}_data'.format(kind)] = item[4]



        # print(name)
        # print(subject)
        # print(lect_nm)
        # print(yoil)
        # print(len(yoil))
        # print(t1)
        # print(t2)


    return mylecture_list, info