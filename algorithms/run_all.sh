#!/bin/bash
echo "Date: `date`"
echo "Python Version: `python -V`"
echo "Testing all algorithms"
pip install flake8
pip install pytest
pip3 install black
flake8 . --count --select=E9,F4,F63,F7,F82 --show-source --statistics
black . || true
black --check . || true
echo "================================================================================================"
for i in `ls *.py`; do echo $i;  
   echo "Test:  $i"
   echo "Running doctest...."
   python -m doctest -v $i
   echo "Running $i"
   time python $i 
   echo "PASS"
done
echo "================================================================================================"
