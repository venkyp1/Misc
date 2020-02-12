'''
Simple REST API using Flask
Runs on Linux/MacOS.
Venky, Sat Jan 11 00:50:28 PST 2020
'''

from flask import Flask, request
import subprocess

app = Flask(__name__)                                   

def get_data(cmd):
    out = subprocess.getoutput(cmd)
    return("<HTML><BODY><PRE>" + out + "</PRE></BODY></HTML>")

@app.route('/stats/version')
def get_version():
    return "Version: 1.0"

@app.route('/stats/df')
def get_df():
    return get_data('df -h')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)         
