# coding:utf-8
import psutil
import time

def initialize():
    global err
    global oldErr
    err = 0
    oldErr = 0

# get network traffic situation
def getNet():
    sent_before = psutil.net_io_counters().bytes_sent
    recv_before = psutil.net_io_counters().bytes_recv
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    sent = (sent_now - sent_before) / 1024
    recv = (recv_now - recv_before) / 1024
    return sent, recv

def loadBalance():
    global err
    global oldErr
    print(err, oldErr)
    sent, recv = getNet()
    if sent >= 10 or recv >= 10:
        time.sleep(1)
    if err > oldErr:
        oldErr = err
        time.sleep(1)

def addErr():
    global err
    err += 1