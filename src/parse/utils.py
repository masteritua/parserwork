import random
from time import sleep
from parse.models import *
import mpu.io

def save_json(data):

    mpu.io.write('data.json', data)



def save_info(array: list) -> None:
    with open('../parser/save/workua2.txt', 'a') as file:
        for line in array:
            file.write(' | '.join(line) + '\n')

def random_sleep():
    sleep(random.randint(1, 4))
