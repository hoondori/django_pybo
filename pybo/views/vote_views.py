from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    질문 추천
    """
    question = get_object_or_404(Question, pk=question_id)
    print(request.user, question.author)
    if request.user == question.author:
        print('here')
        messages.error(request, "본인의 글을 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)