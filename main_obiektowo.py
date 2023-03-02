"""Quiz"""

from json import load, dump
from string import ascii_lowercase


class Question:

    def __init__(self, text: str, answers: list, right_answer: str) -> None:
        self.text = text
        self.answers = answers
        self.right_answer = right_answer

    def check_answer(self, right_answer):
        """metoda do sprawdzania czy wybrano poprawną odpowiedź"""
        return right_answer == self.right_answer

    def __str__(self) -> str:
        output = f'Pytanie: {self.text} \n'
        output += f'Odpowiedzi: \n'

        for letter, answers in zip(ascii_lowercase, self.answers):
            output += f'{letter} - {answers} \n'

        return output


class Game:
    def __init__(self) -> None:
        self.questions = []

    def load_question(self, file_path: str):
        """metoda służąca do załadowania pytań z pliku"""
        with open(file_path, encoding='utf-8') as file:
            questions = load(file)
            for question in questions:
                self.questions.append(
                    Question(
                        text=question['question'],
                        answers=question['answers'],
                        right_answer=question['right_answer']
                    )
                )

    def play(self) -> int:
        points = 0
        for question in self.questions:
            print(question)
            your_answer = input('Wybierz odpowiedź: \n')
            points += 1 if your_answer == question.right_answer else 0

        print(f'Koniec gry, zdobywasz punktów: {points}.')

        return points


game = Game()
game.load_question('pytania.json')
POINTS = game.play()
name = input('Jak masz na imię: \n')

try:
    with open('result.json', encoding='utf-8') as file:
        result = load(file)

except FileNotFoundError:
    result = []

result.append({
    'name': name,
    'points': POINTS
})

with open('result.json', 'w', encoding='utf-8') as file:
    dump(result, file)
