"""
multiprocessing.Pool ex
"""

from multiprocessing import Pool, cpu_count

import logger


def say_hello(name):
    result = 'hello ' + name
    logger.info(result)
    return result


if __name__ == '__main__':
    CPU_NUM = cpu_count()
    NAMES = ['name1', 'name2', 'name3']
    pool = Pool(CPU_NUM)
    result = pool.map(say_hello, NAMES)
    logger.info('names %s', str(result))
