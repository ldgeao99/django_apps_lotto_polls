from django.shortcuts import render, Http404, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # order_by('속성명') : 오름차순, ('-속성명') : 내림차순
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id): # question_id은 url로 전달받은 값

    q = get_object_or_404(Question, pk = question_id) #존재하지 않을 경우 404페이지를 띄움
    return render(request, 'polls/detail.html', {'question' : q})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return  HttpResponse("You're voting on question %s." % question_id)