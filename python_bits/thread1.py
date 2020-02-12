 
######################################################
        # Venky, Mon Aug 21 16:39:22 2017 # 
######################################################
        

from threading import Thread
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def fun(num, msg):
    logging.debug('starting')
    print (msg, num)
    time.sleep(5)
    print (msg, num, " exiting.")
    logging.debug('Exiting')


if __name__ == '__main__':
    threads = []
    for i in range(10):
        Name = "Billa" + str(i)
        thr = Thread(name=Name, target=fun, args=(i, "Thread Number: "))
        threads.append(thr)
        thr.start()
    
    for t in threads:
        print ("Waiting")
        logging.debug('joining %s', t.getName())  # <== name of the thread joins
        tj = t.join()
        print("joined: ",tj)
print ("Done")


