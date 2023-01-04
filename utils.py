import json
import random


def file_open():
    with open('test.json', 'r', encoding='utf-8') as file:
        date = json.load(file)
        l = random.randint(0, len(date) - 1)
        line = date.pop(l)
        file_read(date)
        return line


def file_read(d):
    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(d, file)
