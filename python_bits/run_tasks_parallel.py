 
######################################################
        # Venky, Wed Jan  2 22:43:46 2019 # 
######################################################
        
'''
Running tasks in parallel requires that many number of CPUs.
'''

import logging
from multiprocessing.pool import Pool
from time import time, sleep


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def run_parallel(id):
    print("Task: {} started".format(id))

    # Do something here
    sleep(10)

    print("Task: {} completed".format(id))


def run_all(c):
    ts = time()
    l = range(c)

    with Pool(c) as p:
        p.map(run_parallel, l)

    logging.info('Time taken to complete:  %s seconds', time() - ts)


if __name__ == '__main__':

    # Technically the system should have 'count' number of CPUs
    count = 8

    run_all(count)
