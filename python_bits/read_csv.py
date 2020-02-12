
'''
Script to read and display a csv file
venky 9/4/15
'''

import csv

def x():
  f = open('nl.csv','r')
  d = csv.DictReader(f)
  for l in d:
     print (l)

if __name__ == '__main__':
  x()
