from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.db.models import Q

def index(request):
    """
    pybo 목록 출력
    """
    #입력 파라미터
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어

    #조회
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #제목검색
            Q(content__icontains=kw) | #내용검색
            Q(author__username__icontains=kw) | #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이검색
        ).distinct()
        # subject__contains = kw 대신 subject__icontains = kw 을 사용하면 대소문자를 가리지 않고 찾아준다.

    #페이징처리
    pagintor = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = pagintor.get_page(page)

    # context = {'question_list': question_list}
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

# page = request.GET.get('page', '1')은 http://localhost:8000/pybo/?page=1
# 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용한다.
# 만약 http://localhost:8000/pybo/ 처럼 page값 없이 호출된 경우에는 디폴트로 1이라는 값을 설정한다.
# paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여 주기
# 첫 번째 파라미터 question_list는 게시물 전체를 의미하는 데이터이고 두번째 파라미터 10은 페이지당 보여줄 게시물의 개수이다.
# page_obj = paginator.get_page(page)
# 그리고 paginator를 이용하여 요청된 페이지(page)에 해당되는 페이징 객체(page_obj)를 생성했다.
# 이렇게 하면 장고 내부적으로는 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html',context)