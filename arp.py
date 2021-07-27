from scapy.all import *
import socket

def main():
    
    # 显示网卡信息
    show_interfaces()
    
    # 获取当前IP并设置默认网卡
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    wifi="Realtek USB FE Family Controller #4"
    wifi_in = input("[*]输入你选择的网卡名称(默认为Realtek USB FE Family Controller #4):")
    ip_num = input("[*]请输入扫描的IP段(默认为"+ipaddr+"/24):")
    
    # 判断用户输入的IP以及网卡
    if wifi_in != '':
        wifi=wifi_in
    if ip_num != '':
        ipaddr=ip_num
    else:
        ipaddr+='/24'

    # 构造ARP请求包
    p=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ipaddr)
    
    # 发送ARP请求报并等待回复
    ans,unans=srp(p,iface=wifi,timeout=5)
    print("[+]一共扫描到%d台主机："%len(ans))
    
    result=[]
    for s,r in ans:
    # 解析收到的包，提取出需要的IP地址和MAC地址
        result.append([r[ARP].psrc,r[ARP].hwsrc])
    
    # 将获取的信息进行排序，看起来更整齐一点
    result.sort()
    
    # 打印出局域网中的主机
    for ip,mac in result:
        print("[+]"+ip,'------>',mac)
main()