import random
from time import sleep
from parse.models import *
import json

def save_json(data):

    saveFile = open('data.json', 'w')
    saveFile.write(json.dumps(data))
    saveFile.close()





def save_info(array: list) -> None:
    with open('../parser/save/workua2.txt', 'a') as file:
        for line in array:
            file.write(' | '.join(line) + '\n')

def random_sleep():
    sleep(random.randint(1, 4))
