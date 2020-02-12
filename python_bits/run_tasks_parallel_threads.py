 
######################################################
        # Venky, Thu Jan  3 14:19:31 2019 # 
######################################################

import logging
from concurrent.futures import ThreadPoolExecutor
from time import time, sleep

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def run_parallel(id):
    print("Task: {} started".format(id))

    # Do something here
    sleep(10)

    print("Task: {} completed".format(id))


def doit(count):
    ts = time()
    print("Starting {} threads...".format(count))
    with ThreadPoolExecutor() as executor:
        executor.map(run_parallel, range(count), timeout=30)
    logging.info('Time taken to complete:  %s seconds', time() - ts)


if __name__ == '__main__':
    doit(8)
