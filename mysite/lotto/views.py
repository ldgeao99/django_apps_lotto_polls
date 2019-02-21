from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import GuessNumbers
from .form import PostForm

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos" : lottos}) # 마지막 괄호에 있는건 딕셔너리 형태로 {}상태로 그냥 놔둬도 무관.

def post(request):
    if request.method == "POST":               # html 코드 에서 지정가능
        form = PostForm(request.POST)
        if form.is_valid():                    # form 객체의 속성을 사용자가 입력한 내용으로 교체한다.
            lotto = form.save(commit = False)  # PostFrom 클래스 내부의 Meta클래스에서 명명한 GuessNumbers 객체가 생성됨.(내부의 데이터가 아직 채워지지 않아 아직 DB에 반영을 안시킴)
            lotto.generate()                   # generate함수 내에서 DB 반영을 시킴
            return redirect('lotto:index')           # urls에서 name속성에 맞는 쪽로 연결된다.
    else:
        form = PostForm()
        return render(request, "lotto/form.html", {"form" : form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # pk는 primary key를 의미한다.
    return render(request, "lotto/detail.html", {"lotto" : lotto})