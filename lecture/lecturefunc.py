import re
from datetime import datetime, timedelta
from .models import yoil

# 시간표 테이블 기초 데이터 작업


yoil_list = yoil.objects.order_by('num')
def lecture_time(mylecture_list):

    info = {}
    rowspans = {}
    teacher = {}
    yoil_teacher ={}
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

        t2 = re.compile('[0-9][0-9]:[0-9][0-9]') #시간 두 번째
        t2 = t2.findall(item[8])

        #요일 갯수 만큼 강의명, 요일, 시간을 저장한다.
        for k in range(0, len(yoil)):
            mins = 30
            time_1 = datetime.strptime(t1[k], "%H:%M") #시간간격을 구한다
            time_2 = datetime.strptime(t2[k], "%H:%M")  # 시간간격을 구한다

            if(str(time_2) == '1900-01-01 00:00:00'): #시간이 00:00:00 이면 바꿔준다
                time_2 = datetime.strptime('23:59', "%H:%M")

            time_interval = time_2 - time_1
            print(time_interval)
            term = time_interval / 30
            term = str(term)
            print(term)
            # 0: 13:58
            term = int(term[2:4])

            if(str(time_2) == '1900-01-01 23:59:00'): #time2 가 00:00:00 이면 term에 +1 해준다
                term = term + 1

            print(name)
            print(yoil[k])
            print(term)
            print(time_1)
            print(time_2)

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

                    characters = ":" #강사별시간에서 : 없애준다다
                    set_time = ''.join(x for x in set_time if x not in characters)

                    #중복이 되지 않게 만듬(월_하명래-국어_0900 = 고1_수능영어-09:00) (월_하명래-국어_0930 = 고1_수능영어-09:00)
                    info[f"{yoil[k]}_{name}-{subject}_{set_time}"] = f"{grade}_{lect_nm}-{info_time}" #강의정보

                    #요일별 강사정보(key 중복제거됨 dic tpye)
                    teacher[f'{yoil[k]}_{name}-{subject}_'] = f'{yoil[k]}' #요일별강사리스트

                    # time_cnt rowspan 값
                    rowspans[f"{yoil[k]}_{name}-{subject}_{set_time}"] = term


    # print(info.get('월_배동환_영어_21:00')) dic 값 추출
    # print(info)
    print(list(teacher.values())) #요일
    print(list(teacher.keys())) #강사명

    # 요일별 강사수
    for yoil in yoil_list:
        yoil_teacher[f'{yoil.yoil_nm}'] = list(teacher.values()).count(yoil.yoil_nm)

    # 요일별 강사명 리스트에서 위치 및 요일별 강사명 뽑아내기
    l1 = list(teacher.values())
    l2 = list(teacher.keys())
    M = []
    t = []
    W = []
    T = []
    F = []
    s = []
    S = []
    for yoil in yoil_list:
        for i in range(len(l1)):
            if l1[i] == yoil.yoil_nm:
                if yoil.yoil_nm == '월':
                    M.append(l2[i])
                if yoil.yoil_nm == '화':
                    t.append(l2[i])
                if yoil.yoil_nm == '수':
                    W.append(l2[i])
                if yoil.yoil_nm == '목':
                    T.append(l2[i])
                if yoil.yoil_nm == '금':
                    F.append(l2[i])
                if yoil.yoil_nm == '토':
                    s.append(l2[i])
                if yoil.yoil_nm == '일':
                    S.append(l2[i])


    yoil_dc = [{'M':M}, {'t':t}, {'W':W}, {'T':T}, {'F':F}, {'s':s}, {'S':S}]
    yoil_li = [M, t, W, T, F, s, S]

    yoil_lect_cnt = []
    for i in range(len(yoil_li)):
        yoil_lect_cnt.append(len(yoil_li[i]))


    # print(type(yoil_lect_cnt[0]))
    # print(yoil_teacher)


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

    #return type info:dic, yoil_dc:dic, yoil_li:list, yoil_lect_cnt:list
    return info, yoil_dc, yoil_li, yoil_lect_cnt, rowspans