 
######################################################
        # Venky, Sun Mar 15 22:48:16 2015 # 
######################################################
        

from threading import Thread
import time

def fun(msg):
    print (msg)
    time.sleep(15)
    print (msg, " exiting.")
    

if __name__ == '__main__':
    Name = "Billa"
    thr = Thread(name=Name, target=fun, args=("Test Thread ",))
    thr.start()
    thr.join()
    print ("Done")
