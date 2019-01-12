"""
os.fork() example
"""

import os

import logger

if __name__ == '__main__':
    pid = os.fork()
    if pid == 0:
        logger.info('this is child process. pid: %d, child_pid: %d', os.getpid(), pid)
    else:
        logger.info('this is parent process. pid: %d, child_pid: %d', pid, os.getpid())
