# -*- coding: utf-8 -*-
"""multi_process.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17tVyqeAyFdl5NgXMfrCIN5baB87YbJMy
"""

import multiprocessing
def now(seconds):
        from datetime import datetime
        from time import sleep
        sleep(seconds)
        print('wait', seconds, 'seconds, time is', datetime.utcnow())
if __name__ == '__main__':
        import random
        for n in range(3):
                seconds = random.random()
                proc = multiprocessing.Process(target=now, args=(seconds,))
                proc.start()