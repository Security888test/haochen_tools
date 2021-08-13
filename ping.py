import os
import threading

num=0

def ping_ip(ip):                                           
    # 执行系统ping命令，并将执行结果存放在output中
    output = os.popen('ping  %s'%ip).readlines()
    global num
    # 从output中循环读取数据
    for w in output:
        # 判断每行中是否存在TTL，存在则说明ping通，主机存活
        if str(w).upper().find('TTL')>=0:
            print("[+]",ip,"is alive")
            num+=1
            break

i=0
while(True):
    ip = '10.163.60.'+str(i)
    t = threading.Thread(target=ping_ip,args=(ip,))    # 创建多线程，使用ping_ip函数，传入ip作为参数
    t.start()
    i+=1
    if i==256:
        break
    
        