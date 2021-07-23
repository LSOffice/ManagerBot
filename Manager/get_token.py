import time
from setup import example

if example == None:
    raise AttributeError('ErroNo 2, setup is not completed, please check setup.py')

with open(example + '.txt', "r") as tf:
    time.sleep(1)
    token = tf.readline(59)