from django.contrib import admin

# Register your models here.

# 아래의 코드를 입력해줘야 admin 사이트에 보여진다.
from .models import Question, Choice

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice # 어떤 모델을 입력받을 것인가.
    extra = 1      # 한번에 객체 몇개의 내용을 입력받을 것인가?, 1이어도 짜장,짬뽕을 가지고 있어서 2개 입력칸이 만들어짐.

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date Information", {'fields': ['pub_date'], 'classes': ['collapse']}), # fields는 입력받는 데이터, classes는 속성
    ]
    inlines = [ChoiceInline]                                                     # 함께 입력받을 모델
    list_display = ('question_text', 'pub_date', 'was_published_recently')       # 객체내용으로 보여질 내용
    list_filter = ['pub_date']                                                   # 필터창 추가
    search_fields = ['question_text']                                            # 검색창 추가
admin.site.register(Question, QuestionAdmin)
