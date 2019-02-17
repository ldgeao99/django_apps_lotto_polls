from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # order_by('속성명') : 오름차순, ('-속성명') : 내림차순
    output = " ,".join([q.question_text for q in latest_question_list]) # 리스트를 문자열로 바꿔주고 " ,"로 원소 중간중간 넣어주겠다는 것.
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return  HttpResponse("You're voting on question %s." % question_id)