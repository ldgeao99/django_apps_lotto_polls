from django.shortcuts import render, Http404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # order_by('속성명') : 오름차순, ('-속성명') : 내림차순
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id): # question_id은 url로 전달받은 값
    try:
        q = Question.objects.get(pk = question_id)

    except Question.DoesNotExist:
        raise Http404("Question %s does not exist" % question_id)

    return render(request, 'polls/detail.html', {'question' : q})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return  HttpResponse("You're voting on question %s." % question_id)