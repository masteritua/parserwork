import random
from time import sleep
import json


def save_json(data):
    with open('data.json', 'w') as file:
        file.write(json.dumps(data))


def save_info(array: list) -> None:
    with open('../parser/save/workua2.txt', 'a') as file:
        for line in array:
            file.write(' | '.join(line) + '\n')


def random_sleep():
    sleep(random.randint(1, 4))
