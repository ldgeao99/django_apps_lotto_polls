from django.shortcuts import render, Http404, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.views import generic

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # order_by('속성명') : 오름차순, ('-속성명') : 내림차순
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)
'''

class IndexView(generic.ListView):   # 객체를 리스트 형태로 전달하기 때문에 ListView 선택
    #어떤 템플릿이랑 연결할 것이고, 가져온 오브젝트를 어느 이름으로 mapping 시킬것인지.
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'        # index.html에서 이 이름으로 변수에 접근 가능
    # 오브젝트 가져오기
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

'''
def detail(request, question_id): # question_id은 url로 전달받은 값
    q = get_object_or_404(Question, pk = question_id) #존재하지 않을 경우 404페이지를 띄움
    return render(request, 'polls/detail.html', {'question' : q})

'''
class DetailView(generic.DetailView): # 제네릭뷰의 DetialView를 상속받음
    # 어떤 모델이랑 연결해서 어떤 템플릿으로 넘져줄지
    model = Question
    template_name = 'polls/detail.html'

'''
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

class ResultsView(generic.DetailView): # 제네릭뷰의 DetialView를 상속받음
    # 어떤 모델이랑 연결해서 어떤 템플릿으로 넘져줄지
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice']) # id가 choice인 것의 vlaue 값을 읽어옴
    except:
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else: #예외가 발생하지 않은경우
        selected_choice.votes += 1  # 모델 객체의 값 변경
        selected_choice.save()      # DB에 반영
        #return redirect('polls:results', question_id = question_id)
        return redirect('polls:results', pk=question_id)