from django import forms

from .models import GuessNumbers     # GuessNumbers의 입력받을 폼을 만드는 것이므로

class PostForm(forms.ModelForm):     # 폼을 만들 때 forms.ModelForm을 상속받는건 일반적이다.
    class Meta:
        model = GuessNumbers         # 어떤 모델에 대한 입력 form을 만들래?
        fields = ('name', 'text',)   # 그중에 어떤 속성을 입력받을래?

