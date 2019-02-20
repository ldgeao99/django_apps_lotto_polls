from django.test import TestCase

# Create your tests here.
import  datetime
from django.utils import  timezone
from .models import Question

class QuestionMethodsTests(TestCase):
    # 7일 미래의 시간을 테스트하는 코드
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=7)      # 현재 + 7일 즉, 미래의 날짜.
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    # 30일 전의 시간을 테스트 하는 코드
    def test_was_published_recently_with_old_question(self):
        """ was_published_recently() should return False for questions whose pub_date is older than 1 day. """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # 1시간 전의 시간을 테스트 하는 코드
    def test_was_published_recently_with_recent_question(self):
        """ was_published_recently() should return True for questions whose pub_date is within the last day. """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


