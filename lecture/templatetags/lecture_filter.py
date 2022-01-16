from django import template
import re

register = template.Library()

@register.filter
def grade(value):
    p = re.compile('[가-하][1-9]')
    m = p.findall(value)
    return m

@register.filter
def yoil(value):
    p = re.compile('[가-하]')
    m = p.findall(value)
    return m

@register.filter
def timeis(value):
    p = re.compile('[0-9][0-9]:[0-9][0-9]')
    m = p.findall(value)
    return m

@register.filter
def yoil_cnt(value):
    p = re.compile('[가-하]')
    m = p.findall(value)
    cnt = len(m)
    return cnt

@register.filter
def cut_text(value):
    result = value[0:20]
    return result

@register.filter
def comma(value):
    result = (format(int(value),","))
    return result

@register.simple_tag
def yoil_time(yoil, time1, time2):
    p_yoil = re.compile('[가-하]')
    m_yoil = p_yoil.findall(yoil)

    p_time1 = re.compile('[0-9][0-9]:[0-9][0-9]')
    m_time1 = p_time1.findall(time1)

    p_time2 = re.compile('[0-9][0-9]:[0-9][0-9]')
    m_time2 = p_time2.findall(time2)

    p=[]
    for i in range(0,len(m_yoil)):
        a = m_yoil[i]
        b = m_time1[i]
        c = m_time2[i]
        # print(a)
        p.append(a+b+"-"+c)

    return p