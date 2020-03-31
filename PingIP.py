import os
import time
import sys

def readFromFile():
    os.system('cls')
    path = cwd = os.getcwd()
    print("Reading file from file\n" + path + "ip-target.txt")
    time.sleep(2)

    with open('ip-target.txt') as file:
        dump = file.read()
        dump = dump.splitlines()

        for ip in dump:
            os.system('cls')
            print('Pinging:', ip)
            os.system('ping -n 2 {}'.format(ip))     

            print('-'*60)
            time.sleep(5)

def customIP():
    os.system('cls')
    print("Enter IP Address: ", end='')

    ip = input()

    os.system('cls')
    print('Pinging:', ip)
    os.system('ping -n 2 {}'.format(ip))     

    print('-'*60)
    time.sleep(5)

while(True):
    os.system('cls')   

    print("Ping Menu:\n")
    print("1) Read IP's from ip-targets.txt.")
    print("2) Input custom IP to ping.")
    print("3) Exit.")
    print("\n\nEnter #: ", end='')

    try:
        i = int(input())

        if(i==1):
            readFromFile()
        elif(i==2):
            customIP()
        elif(i==3):
            break
    except:
        #loop restarts
        print("Error!")