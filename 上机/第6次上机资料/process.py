# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:33:41 2019

@author: Lenovo
"""

import random
class PCB:
    def __init__(self,pid,arr_time,all_time,cpu_time,state): ##初始化进程
        self.pid=pid
        self.arr_time=arr_time
        self.all_time=all_time
        self.cpu_time=cpu_time
        self.state=state

    def Output(self):   ##sjf fcfs输出
        print("进程"+str(self.pid),"正在执行，到达时间:"+str(self.arr_time),
              "还需运行时间:"+str(self.all_time),"已运行时间:"+str(self.cpu_time))

    def toRun(self):    ##将状态置为Run
        self.state="Run"
    def toFinish(self):     ##将状态置为Finish
        self.state="Finish"
    def toReady(self):      ##将状态置为Ready
        self.state="Ready"
    def running(self):      ##进程运行时状态变化
        self.all_time-=1
        self.cpu_time+=1


def init(num):##初始化进程，生成四个进程并按到达时间将它们放入列表list1
    list1=[]
    for i in range(num):
        list1.append(PCB(str(i),random.randint(10,15),
                         random.randint(1,10),0,"Ready"))
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i].arr_time>list1[j].arr_time:
                list1[i],list1[j] = list1[j],list1[i]
    return list1
        
def fcfs(list1):##先来先服务
    time=0
    while 1:
        print("time:",time)
        if time>=list1[0].arr_time:
            list1[0].running()
            list1[0].Output()
            if list1[0].all_time==0:
                print("进程"+list1[0].pid+"执行完毕,周转时间："+str(time-list1[0].arr_time+1)+"\n")
                list1.remove(list1[0])
        time+=1
        if not list1:
            break

if __name__=="__main__":
    while 1:
        n=input("请选择算法(1、先来先服务):")
        if n=="1":
            list1=init(4)
            for i in list1:
                i.Output()
            fcfs(list1)
        else:
            print("输入错误，请重新输入！")