import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizsite.settings')
django.setup()

from quiz.models import QuizQuestion

# Список вопросов для заполнения базы данных
questions = [
    # История
    {"subject": "history", "question": "Была ли Американская Революция в 18 веке?", "answer": True},
    {"subject": "history", "question": "Произошло ли Крещение Руси в 10 веке?", "answer": True},
    {"subject": "history", "question": "Существовал ли Римский Император Гай Юлий Цезарь?", "answer": True},
    {"subject": "history", "question": "Была ли Первая Мировая Война в 20 веке?", "answer": True},
    {"subject": "history", "question": "Существовали ли древние олимпийские игры в Греции?", "answer": True},
    {"subject": "history", "question": "Произошло ли падение Берлинской стены в 1991 году?", "answer": False},
    {"subject": "history", "question": "Был ли Конфликт в Корее в 1950-1953 годах?", "answer": True},
    {"subject": "history", "question": "Существовал ли Египетский фараон Рамзес II?", "answer": True},
    {"subject": "history", "question": "Была ли Великая Французская революция в конце 18 века?", "answer": True},
    {"subject": "history", "question": "Произошло ли Падение Римской Империи в 5 веке н.э.?", "answer": True},

    # Химия
    {"subject": "chemistry", "question": "Вода состоит из молекул H2O?", "answer": True},
    {"subject": "chemistry", "question": "Углекислый газ безвреден для человека?", "answer": False},
    {"subject": "chemistry", "question": "Кислота реагирует с основанием, образуя соль и воду?", "answer": True},
    {"subject": "chemistry", "question": "Сера — это металл?", "answer": False},
    {"subject": "chemistry", "question": "Химическая реакция может изменять цвет вещества?", "answer": True},
    {"subject": "chemistry", "question": "Стекло является химическим элементом?", "answer": False},
    {"subject": "chemistry", "question": "Железо может быть окислено?", "answer": True},
    {"subject": "chemistry", "question": "Кислота обладает щелочными свойствами?", "answer": False},
    {"subject": "chemistry", "question": "Соли образуются в результате реакции кислоты и кислоты?", "answer": False},
    {"subject": "chemistry", "question": "Алюминий реагирует с кислотой, выделяя водород?", "answer": True},

    # Биология
    {"subject": "biology", "question": "Клетка — базовая структурная и функциональная единица всех живых организмов?", "answer": True},
    {"subject": "biology", "question": "Вирусы — это живые организмы?", "answer": False},
    {"subject": "biology", "question": "Человек имеет одно сердце?", "answer": True},
    {"subject": "biology", "question": "ДНК содержит информацию о наследственности?", "answer": True},
    {"subject": "biology", "question": "Растения проводят фотосинтез?", "answer": True},
    {"subject": "biology", "question": "Бактерии могут вызывать инфекционные болезни?", "answer": True},
    {"subject": "biology", "question": "Рыбы — это позвоночные животные?", "answer": True},
    {"subject": "biology", "question": "Клеточное ядро присутствует в прокариотических клетках?", "answer": False},
    {"subject": "biology", "question": "Грибы относятся к растениям?", "answer": False},
    {"subject": "biology", "question": "Животные могут дышать кислородом?", "answer": True},

    # Физика
    {"subject": "physics", "question": "Свет движется быстрее, чем звук?", "answer": True},
    {"subject": "physics", "question": "Твердые тела имеют форму и объем?", "answer": True},
    {"subject": "physics", "question": "Электрический ток может проходить через воду?", "answer": True},
    {"subject": "physics", "question": "Энергия не может быть уничтожена, только преобразована?", "answer": True},
    {"subject": "physics", "question": "Сила притяжения между двумя объектами уменьшается с увеличением расстояния между ними?", "answer": True},
    {"subject": "physics", "question": "Звук может распространяться в вакууме?", "answer": False},
    {"subject": "physics", "question": "Температура измеряется в градусах Цельсия?", "answer": True},
    {"subject": "physics", "question": "Кинетическая энергия зависит от массы и скорости объекта?", "answer": True},
    {"subject": "physics", "question": "Магнитный полюс всегда притягивает другой магнитный полюс?", "answer": False},
    {"subject": "physics", "question": "Все объекты падают с одинаковым ускорением?", "answer": True},

    # География
    {"subject": "geography", "question": "Африка — это страна?", "answer": False},
    {"subject": "geography", "question": "Гималаи — самые высокие горы в мире?", "answer": True},
    {"subject": "geography", "question": "Австралия — самый большой континент по площади?", "answer": False},
    {"subject": "geography", "question": "Антарктида — это континент?", "answer": True},
    {"subject": "geography", "question": "Москва — столица России?", "answer": True},
    {"subject": "geography", "question": "Атлантический океан самый большой океан?", "answer": False},
    {"subject": "geography", "question": "Северный полюс расположен на континенте?", "answer": False},
    {"subject": "geography", "question": "Европа — это континент?", "answer": True},
    {"subject": "geography", "question": "Амазонка — самая длинная река в мире?", "answer": True},
    {"subject": "geography", "question": "Сахара — это пустыня?", "answer": True},

    {"subject": "math", "question": "2 + 2 = 4?", "answer": True},
    {"subject": "math", "question": "3 × 5 = 20?", "answer": False},
    {"subject": "math", "question": "9 - 6 = 3?", "answer": True},
    {"subject": "math", "question": "10 ÷ 2 = 5?", "answer": True},
    {"subject": "math", "question": "4^2 = 16?", "answer": True},
    {"subject": "math", "question": "12 × 3 = 36?", "answer": True},
    {"subject": "math", "question": "15 - 8 = 7?", "answer": True},
    {"subject": "math", "question": "20 ÷ 4 = 6?", "answer": False},
    {"subject": "math", "question": "5^3 = 125?", "answer": True},
    {"subject": "math", "question": "16 - 9 = 7?", "answer": False},
]

# Создание записей в базе данных
for question in questions:
    QuizQuestion.objects.create(**question)

print("База данных успешно заполнена вопросами.")
