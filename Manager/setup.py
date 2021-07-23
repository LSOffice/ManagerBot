import os
import time
import datetime
from log.logger import Log

example = None
current = datetime.date.today()

def Setup(filename='config'):
    print('Configurating files')
    os.system('clear')
    global example
    example = filename
    try:
        open(filename + '.txt', "x")
    except FileExistsError:
        print(f'{example}.txt already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'{example}.txt', loc=1)
    try:
        open(f'./log/{current}_log.txt', "x")
    except FileExistsError:
        print(f'{current}_log.txt already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'{current}_log.txt', loc=1)
    try:
        open(f'./log/{current}_auditlog.txt', "x")
    except FileExistsError:
        print(f'{current}_auditlog.txt already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'{current}_auditlog.txt', loc=1)
    try:
        open(f'./levelling/users.json', "x")
    except FileExistsError:
        print(f'users.json already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'users.json.txt', loc=1)
    try:
        open(f'./settings/levelup_messages.json', "x")
    except FileExistsError:
        print(f'settings.json already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'settings.json.txt', loc=1)
    try:
        open('./settings/prefix.json', "x")
    except FileExistsError:
        print('prefix.json already exists, skipping [1] line of code')
        Log("FileExistsError", filename='prefix.json', loc=1)
    try:
        open(f'./settings/levelup_channels.json', "x")
    except FileExistsError:
        print(f'settings.json already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'settings.json.txt', loc=1)
    try:
        open(f'./settings/blocked_slurs.json', "x")
    except FileExistsError:
        print(f'block_slursed.json already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'settings.json.txt', loc=1)
    try:
        open(f'./settings/blocked_swears.json', "x")
    except FileExistsError:
        print(f'blocked_swears.json already exists, skipping [1] line of code')
        Log("FileExistsError", filename=f'settings.json.txt', loc=1)


Setup("config")