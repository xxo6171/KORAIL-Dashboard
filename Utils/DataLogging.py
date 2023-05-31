import os
import sys
from os import path
import time
import random
import numpy as np
import multiprocessing as mp

# todo: Convert Text data to Numpy array
def txt2Numpy(filepath):
    return np.loadtxt(filepath, dtype=np.uint16, delimiter=' ')

# todo: Get File data to numpy array
def getDataNumpy(date: str):
    filepath = [f'LogData/{date}/widget{i}.txt' for i in range(1, 12)]
    for file in filepath:
        if not path.exists(file):
            return None
    return np.array(list(map(txt2Numpy, filepath))).copy()

# todo: Get File data to numpy array using Parallel
def getDataNumpyParallel(date):
    filepath = [f'LogData/widget{i}_{date}.txt' for i in range(1, 12)]
    for file in filepath:
        if not path.exists(file):
            return None
    pool = mp.Pool(processes=mp.cpu_count())
    result = np.array(list(pool.map(txt2Numpy, filepath)))
    pool.close()
    pool.join()
    return result.copy()

def dataLogging(widget, date):
    if not os.path.isdir(f'../LogData/{date}'):
        os.mkdir(f'../LogData/{date}')

    for i in range(1, 12):
        t = 1
        filepath = f'../LogData/{date}/{widget}{i}.txt'
        with open(filepath, "w" if not path.exists(filepath) else "a") as f:
            while True:
                try:
                    if t == 86400:
                        break
                    # t = time.strftime('%H%M%S')
                    value = random.randrange(100, 201)
                    data = f'{t} {value}\n'
                    f.write(data)
                    t += 1
                except KeyboardInterrupt:
                    sys.exit(0)


if __name__ == '__main__':
    date = time.strftime('%Y%m%d')
    dataLogging('widget', date)

