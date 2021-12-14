from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() #get방식으로 넘어 왔을때 QuestionForm을 인수 없이 생성한다.
    context = {'form': form}
    return render(request, 'pybo/question_create.html', context)

# GET 방식에서는 form = QuestionForm() 처럼 QuestionForm을 인수 없이 생성했다. 하지만 POST 방식에서는
# form = QuestionForm(request.POST) 처럼 request.POST를 인수로 생성했다. request.POST를
# 인수로 QuestionForm을 생성할 경우에는 request.POST에 담긴 subject, content 값이 QuestionForm의 subject, content 속성에
# 자동으로 저장되어 객체가 생성된다.
# request.POST에는 화면에서 사용자가 입력한 내용들이 담겨있다.
#
# 그리고 form.is_valid()는 form이 유효한지를 검사한다.
# 만약 form에 저장된 subject, content의 값이 올바르지 않다면 form에는 오류 메시지가 저장되고
# form.is_valid()가 실패하여 다시 질문 등록 화면으로 돌아갈 것이다.
# 이 때 form에 저장된 오류 메시지는 질문 등록 화면에 표시된다.
#
# form이 유효하다면 if form.is_valid(): 이후의 문장이 수행되어 질문 데이터가 생성된다.
# question = form.save(commit=False)는 form으로 Question 데이터를 저장하기 위한 코드이다.
# QuestionForm이 Question 모델과 연결된 모델 폼이기 때문에 이와 같이 사용할 수 있다.
# 여기서 commit=False는 임시 저장을 의미한다.
# 즉, 실제 데이터는 아직 데이터베이스에 저장되지 않은 상태를 말한다.
# 여기서 form.save(commit=False) 대신 form.save()를 수행하면
# Question 모델의 create_date에 값이 없다는 오류가 발생한다.
# 왜냐하면 QuestionForm에는 현재 subject, content 속성만 정의되어 있고 create_date 속성은 없기 때문이다.
# 이러한 이유로 임시 저장을 한 후 question 객체를 리턴받아 create_date에 값을 설정한 후 question.save()로 실제 저장하는 것이다.
#
# create_date 속성은 데이터 저장 시점에 자동 생성해야 하는 값이므로 QuestionForm에 등록하여 사용하지 않는다.
# 그리고 마지막으로 저장이 완료되면 return redirect('pybo:index')를 호출하여 질문 목록 화면으로 이동한다.

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_create.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')