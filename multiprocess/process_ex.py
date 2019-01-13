"""
multiprocessing.Process 예제
"""

from multiprocessing import Process

import logger


def say_hello(name):
    logger.info('hello %s', name)


if __name__ == '__main__':
    process1 = Process(target=say_hello, args=('process1',))
    process2 = Process(target=say_hello, args=('process2',))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
