import os, sys
os.system('git pull')
try:
    __import__("Psycho").bnsreg()
except Exception as e:
    exit(str(e))
 
