from django.contrib import admin

# Register your models here.

# 아래의 코드를 입력해줘야 admin 사이트에 보여진다.
from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)