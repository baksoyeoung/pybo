import re
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



        print(name)
        print(subject)
        print(lect_nm)
        print(yoil)
        print(len(yoil))
        print(t1)
        print(t2)


    return mylecture_list