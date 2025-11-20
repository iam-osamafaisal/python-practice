import os
##  --import datetime

command = "df -h" # disk
command = "uptime" # load avg
command = "date" # date

def check_cup(command): # defining a function
    print(os.system(command))

def check_date(command): # defining a function
    print(os.system(command))    


def check_ram(command):
    print(os.system(command))

check_date("sysinfo") # calling a function