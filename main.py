from utils import file_open


class Answer:
    def __init__(self, q, d, a, x=None):
        self.x = x
        self.q = q
        self.d = d
        self.a = a

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов. """
        return int(self.d) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает с верным ответов иначе False. """
        return self.a == self.x

    def build_positive_feedback(self):
        """Возвращает ответ верный, получено _ баллов"""
        return f'Ответ верный, получено {int(self.d)*10} баллов'

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ _"""
        return f'Ответ неверный. Верный ответ - {self.a}'


class Question(Answer):
    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5"""
        return f"\n Вопрос: {self.q} \nСложность: {self.d}/5"

# answer = input()


def final():
    try:
        total = 0
        count = 0
        while True:
            line = file_open()
            question = Question(line['q'], line['d'], line['a'])
            print(question.build_question())
            x = input()
            answer = Question(line['q'], line['d'], line['a'], x)
            if answer.is_correct():
                print(answer.build_positive_feedback())
                count += answer.get_points()
                total += 1
            else:
                print(answer.build_negative_feedback())
    except ValueError:
        print()
        print('Вот и все!')
        print(f'Отвечено {total} вопроса из 10')
        print(f'Набрано баллов: {count}')

final()

