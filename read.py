import sys
import os

path = str(sys.argv[1])
find = str(sys.argv[2])
print(path+'+++'+find)
#path = input("请输入日志所在目录路径：")
#path = 'D:\work\恒睿达\www\日志'
#find = input("请输入查找的内容：")
get_dir = os.listdir(path)
wp=open(path+'\\'+'find.txt',"w")
for i in get_dir:
    try:
        i = path+'\\'+i
        fp = open(i,"r")
        #print(i+"文件打开成功")
        strr = fp.read()
        fp.close()
        str=strr.splitlines()
        #print(str[0])
        for j in str:
            #print(j)
            if find in j:
                print(j)
                print(j,file=wp)
    except IOError:
        print(i+"文件打开错误")
wp.close()
