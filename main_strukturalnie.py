
"""Quiz"""
from string import ascii_lowercase
from json import load

with open('pytania.json', encoding='utf-8') as file:
    questions = load(file)
    points = 0
    for question in questions:
        print('---' * 20)
        print('Pytanie:', question['question'])
        print('Odpowiedź:')
        for letter, answer in zip(ascii_lowercase, question['answers']):
            print(f'{letter} - {answer}')

        your_answer = input("Wybierz odpowiedź: ")

        points += 1 if your_answer == question['right_answer'] else 0

print('Koniec gry!')
print('Zdobyłes punktów: ', points)
