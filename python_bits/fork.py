'''
using fork
Venky, 12/10/2016
'''

import os
import time

def  pyramid(lines, char):

    spc  = lines
    char = char + ' '
    for i in range(1, lines+1):
        sp = ' ' * (spc - 1)
        chars = char * i
        print(sp + chars)
        spc -= 1
    time.sleep(5)


if __name__ == '__main__':

  pid = os.fork()
  
  # Successful fork() will return 0 to the chile process and >0 to parent process
 
  if pid == 0:
    #Child Process
    pyramid(10, '*')
    print("Child PID: ", os.getpid())
  else: 
    #Parent Process
    print("Parent PID: ", os.getpid())
    pyramid(20, '*')
    time.sleep(4)
    os.wait()  # Wait till the child exits
