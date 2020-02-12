 
######################################################
        # Venky, Tue Aug 22 07:31:02 2017 # 
######################################################
        

import threading 
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def fun(num, msg):
    msg += str(num)
    #logging.debug('starting')
    print (msg, num)
    readData()
    writeData(msg)
    #logging.debug('Exiting')

def writeData(m):
    lock = threading.Lock()
    lock.acquire()
    try:
      fw = open('/tmp/message', 'w+')
    except Exception as e:
       print(e)
    fw.write(m)
    lock.release()
    fw.close()

def readData():
    lock = threading.Lock()
    if os.path.isfile('/tmp/message'):
      try:
        fr = open('/tmp/message', 'r')
      except Exception as e:
        print(e)
      lock.acquire()
      msg = fr.read()
      print("Message: ",msg)
      lock.release()
      fr.close() 

if __name__ == '__main__':
    threads = []
    for i in range(10):
        Name = "Billa" + str(i)
        thr = threading.Thread(name=Name, target=fun, args=(i, "Thread Number: "))
        threads.append(thr)
        thr.start()
    
    for t in threads:
        print ("Waiting")
        logging.debug('joining %s', t.getName())  # <== name of the thread joins
        t.join()
print ("Done")

