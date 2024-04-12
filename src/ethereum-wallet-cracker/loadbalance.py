# coding:utf-8
import psutil
import time
import numpy as np
import matplotlib.pyplot as plt

def initialize():
    global err
    global oldErr
    global sent_before
    global recv_before
    global itrErr
    err = 0
    oldErr = 0
    sent_before = psutil.net_io_counters().bytes_sent
    recv_before = psutil.net_io_counters().bytes_recv
    itrErr = {}

# get network traffic situation
def getNet():
    global sent_before
    global recv_before
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    sent = (sent_now - sent_before) / 1024
    recv = (recv_now - recv_before) / 1024
    sent_before = sent_now
    recv_before = recv_now
    return sent, recv

def loadBalance():
    global err
    global oldErr
    # print(err, oldErr)
    sent, recv = getNet()
    if sent >= 10 or recv >= 10:
        time.sleep(1)
    if err > oldErr:
        oldErr = err
        time.sleep(1)

def printErr():
    global err
    print(err)
    x = np.arange(0, 40, 1)
    y = []
    for p in range(0, 40):
        y.append(itrErr.get(p, 0))
    plt.plot(x, y)
    plt.title('err rate with load balancing')
    plt.show()
    

def addErr(i):
    global err
    global itrErr
    err += 1
    ct = itrErr.get(i, 0) + 1
    itrErr[i] = ct