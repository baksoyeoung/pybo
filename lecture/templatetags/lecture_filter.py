from django import template
from django.template.defaultfilters import stringfilter
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
def timeis_ranges_total(value):
    p = re.compile('[0-9][0-9]:[0-9][0-9]')
    m = p.findall(value)
    cnt = len(m)
    return range(0, cnt)

@register.simple_tag
def time_select(value, cnt):
    print(value, cnt)
    p = re.compile('[0-9][0-9]:[0-9][0-9]')
    m = p.findall(value)
    return m[cnt]

@register.filter
def yoil_cnt(value):
    p = re.compile('[가-하]')
    m = p.findall(value)
    cnt = len(m)
    return cnt

@register.filter()
def yoil_ranges(value):
    p = re.compile('[가-하]')
    m = p.findall(value)
    cnt = len(m)
    return range(2, cnt+1)

@register.filter()
def yoil_ranges_total(value):
    p = re.compile('[가-하]')
    m = p.findall(value)
    cnt = len(m)
    return range(0, cnt)

@register.simple_tag
def yoil_select(value, cnt):
    p = re.compile('[가-하]')
    m = p.findall(value)
    return m[cnt]

@register.filter()
def gains(value):
    value = value + 1
    return value

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
