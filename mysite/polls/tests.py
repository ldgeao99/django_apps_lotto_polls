from django.test import TestCase

# Create your tests here.
import  datetime
from django.utils import  timezone
from .models import Question
from django.urls import reverse

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date = time)

class QuestionViewTests(TestCase):
    def test_index_view_with_future_question(self):
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)                            # 상태코드가 200이야?
        self.assertQuerysetEqual(response.context['latest_question_list'], []) # 쿼리셋 결과가 []이야?

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


