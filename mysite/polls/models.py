from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published') # ( ) 에 들어간 텍스트는 그냥 주석이다.


class Choice(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)