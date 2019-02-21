from django.contrib import admin
from .models import GuessNumbers # lotto.models == .models 이는 같은 모듈안에 있기 때문에 생략이 가능한 것임
# Register your models here.

admin.site.register(GuessNumbers)