from django.test import TestCase

# Create your tests here.
import  datetime
from django.utils import  timezone
from .models import Question
from django.urls import reverse

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date = time)

class QuestionViewTests1(TestCase):
    def test_index_view_with_future_question(self):
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)                            # 상태코드가 200이야?
        self.assertQuerysetEqual(response.context['latest_question_list'], []) # 쿼리셋 결과가 []이야?

class QuestionViewTests2(TestCase):
    # 아무 객체도 없는경우 아무것도 안보여줌을 테스트.
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")    # 아무것도 없는경우 "No polls..."가 찍여야 함(index.html참고)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 과거의 날짜를 가진 객체는 보여짐을 테스트.
    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # 미래의 날짜를 가진 객체는 보이지 않아야 함을 테스트.
    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 과거의 날자와 미래의 날짜를 가진 객체가 모두 존재한다면 과거의 날짜를 가진 객체만 보여야함을 테스트.
    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    # 2개의 과거 날짜를 가진 객체가 있을 때 둘 다 보여지며, 시간순서대로 잘 정렬되어 나오는지 테스트.
    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

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


