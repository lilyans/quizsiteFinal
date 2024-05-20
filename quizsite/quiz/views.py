from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import QuizQuestion
from .forms import QuizForm

def index(request):
    return render(request, "index.html")



class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        data = form.data
        subject = f'Вопрос от {data["email"]}'
        text = f'Заявка от {data["first_name"]}. Вопрос {data["question"]}'
        email(subject, text)
        return super().form_valid(form)


def email(subject, content):
    send_mail(
        subject,
        content,
        'anisovich.le@phystech.edu',
        ['anisovich.le@phystech.edu']
    )

def quiz_view(request, subject):
    questions = QuizQuestion.objects.filter(subject=subject)
    template_name = f'quiz.html'  # Использование динамического выбора шаблона
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                user_answer = form.cleaned_data[f'question_{question.id}'] == 'True'
                if user_answer == question.answer:
                    score += 1
            return render(request, 'result.html', {'score': score, 'total': questions.count(), 'subject': subject})
    else:
        form = QuizForm(questions=questions)
    return render(request, template_name, {'form': form, 'subject': subject})
