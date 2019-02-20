from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published') # ( ) 에 들어간 텍스트는 그냥 주석이다.

    # 객체를 그대로 출력할 때 객체의 내용을 보여주도록 오버라이딩
    def __str__(self):
        return self.question_text
    # 객체가 가지고 있는 날짜 >= 하루전의 시간(어제)라면 True
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    # 객체를 그대로 출력할 때 객체의 내용을 보여주도록 오버라이딩
    def __str__(self):
        return self.choice_text