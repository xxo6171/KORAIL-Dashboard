import sys
from os import path
import time
import random
import numpy as np
import multiprocessing as mp

# todo: Convert Text data to Numpy array
def txt2Numpy(filepath):
    return np.loadtxt(filepath, dtype=int, delimiter=' ')

# todo: Get File data to numpy array
def getDataNumpy(date):
    filepath = [f'../LogData/widget{i}_{date}.txt' for i in range(1, 12)]
    for file in filepath:
        if not path.exists(file):
            return None
    return np.array(list(map(txt2Numpy, filepath)))

# todo: Get File data to numpy array using Parallel
def getDataNumpyParallel(date):
    filepath = [f'../LogData/widget{i}_{date}.txt' for i in range(1, 12)]
    for file in filepath:
        if not path.exists(file):
            return None
    pool = mp.Pool(processes=mp.cpu_count())
    result = np.array(list(pool.map(txt2Numpy, filepath)))
    pool.close()
    pool.join()
    return result

# def txt2List(filepath):
#     with open(filepath, 'r') as f:
#         return [s.strip().split() for s in f.readlines()]
#
# def getDataList(date):
#     filepath = [f'../LogData/widget{i}_{date}.txt' for i in range(1, 12)]
#     for file in filepath:
#         if not path.exists(file):
#             return None
#     return list(map(txt2List, filepath))

def dataLogging(widget, date):
    for i in range(1, 12):
        t = 1
        filepath = f'../LogData/{widget}{i}_{date}.txt'
        with open(filepath, "w" if not path.exists(filepath) else "a") as f:
            while True:
                try:
                    if t == 86400:
                        break
                    # t = time.strftime('%H%M%S')
                    value = random.randint(190, 201)
                    data = f'{t} {value}\n'
                    f.write(data)
                    t += 1
                except KeyboardInterrupt:
                    sys.exit(0)

# if __name__ == '__main__':
    # a = np.uint8(100)
    # b = np.uint16(100)
    # c = 12
    # d = 'widget_'
    # e = np.string_('widget_')
    #
    # print(sys.getsizeof(a))
    # print(sys.getsizeof(b))
    # print(sys.getsizeof(c))
    # print(sys.getsizeof(d))
    # print(sys.getsizeof(e))
    # print(sys.getsizeof(12))

    # date = time.strftime('%Y%m%d')
    # dataLogging('widget', date)
    # print('Writing Done')
    # # file_size = os.path.getsize('../LogData/widget1_20230417.txt')
    # # print("파일 크기: %.2fMB" % (file_size / (1024.0 ** 2)))
    #
    # start_time = time.time()
    # result1 = getDataNumpy(date)
    # end_time = time.time()
    # print('numpy execution time: ', end_time - start_time)
    #
    # start_time = time.time()
    # result2 = getDataNumpyParallel(date)
    # end_time = time.time()
    # print('Parallelized numpy execution time: ', end_time - start_time)
    #
    # print('numpy shape: ', result1.shape)
    # print('numpy shape: ', result2.shape)
    # print('Compare two arrays for equality: ', np.array_equal(result1, result2))

