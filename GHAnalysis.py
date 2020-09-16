import ujson
import os
import sys
import getopt
import time
import threading
def read_1(path):
    global count,path_all
    path_all = []
    for root, dirs, files in os.walk(path):
        for file in files:   
            path_all.append(os.path.join(root, file))
    count = len(path_all)
def ooopen(a,b):
    global data
    data = []
    for i in range(a,b):
        with open(path_all[i],'r',encoding='utf8')as f:
            for line in f:
                data.append(ujson.loads(line))
    sum.append(find_data())
def get_cmd():
    global path,user,repo,event,judger,length
    path,user,repo,event = 'djista','djista','djista','djista'
    opt,arv= getopt.getopt(sys.argv[1:],'i:u:r:e:',['user=','repo=','event=','init='])
    if len(opt):
        length = len(opt)
        for i in range(0,len(opt)):
            if opt[i][0] == '-i':
                path = opt[i][1]
            elif opt[i][0] == '-u':
                user = opt[i][1]
                judger = 1
            elif opt[i][0] == '-r':
                repo = opt[i][1]
                judger = 2
            elif opt[i][0] == '-e':
                event = opt[i][1]
def find_data():
    result = 0
    for i in range(0,len(data)):
        data_str = str(data[i])
        if judger ==  1:
            if user in data_str :
                if event in data_str:
                    result = result +  1
        if judger == 2:
            if length == 3:
                if data_str.find(repo) != -1:
                    if data_str.find(event) != -1:
                        result = result +  1
            else:
                if data_str.find(repo) != -1:
                    if data_str.find(event) != -1:
                        if data_str.find(user)!= -1:
                            result = result +  1
    return result

if __name__ == '__main__':
    sum =[]
    start_time = time.time()
    get_cmd()
    read_1(path)
    t1 = threading.Thread(target=ooopen,args=(0,2))
    t2 = threading.Thread(target=ooopen,args=(2,4))
    t3 = threading.Thread(target=ooopen,args=(4,6))
    t4 = threading.Thread(target=ooopen,args=(6,count))
    #t3 = threading.Thread(target=find_data)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t4.join()
    print(sum[0]+sum[1]+sum[2]+sum[3])
    end_time = time.time()  # 记录程序结束运行时间
    print('Took %f second3' % (end_time - start_time))
