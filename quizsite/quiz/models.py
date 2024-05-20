from django.db import models

class Contact(models.Model):

    first_name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(max_length=200, verbose_name="Электронная почта")
    question = models.TextField(max_length=800, verbose_name="Вопрос")

    def __str__(self):
        return self.email



class QuizQuestion(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Математика'),
        ('history', 'История'),
        ('chemistry', 'Химия'),
        ('biology', 'Биология'),
        ('physics', 'Физика'),
        ('geography', 'География'),
    ]

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    question = models.TextField()
    answer = models.BooleanField()  # True для "да", False для "нет"

    def __str__(self):
        return f'{self.get_subject_display()} - {self.question}'
