from django.test import TestCase
from .models import GuessNumbers
# Create your tests here.

class GuessNumbersTestCase(TestCase): # TestCase 클래스를 상속받은 클래스
    def test_generate(self):
        g = GuessNumbers(name='apple', text='pineapple')
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20) # ( ) 안의 조건을 만족할 경우 터미널 창에서 OK가 결과가 뜨고 아니면 FAIL이 결과로 뜸