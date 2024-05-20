from django.forms import ModelForm, EmailInput, Textarea
from django.forms import TextInput
from .models import Contact
from django import forms
from .models import QuizQuestion


class ContactForm(ModelForm):

     class Meta:
         model = Contact

         fields = ['first_name', 'email', 'question']
         widgets = {
             'first_name': TextInput(
                 attrs={
                     'placeholder': 'Иван',
                     'class': "myfield",
                 }
             ),
             'email': EmailInput(
                 attrs={
                     'placeholder': 'example@com',
                     'class': "myfield",
                 }
             ),
             'question': Textarea(
                 attrs={
                     'placeholder': 'Ваш вопрос',
                     'class': "myfield",
                 }
             ),
         }


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)

        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.question,
                choices=[(True, 'Да'), (False, 'Нет')],
                widget=forms.RadioSelect
            )
