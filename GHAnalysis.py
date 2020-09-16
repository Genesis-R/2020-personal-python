import json
import os
import sys
import getopt
def read(path):
    global data
    data = []
    path_all = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path_all.append(os.path.join(root, file))
    for i in range(0,len(path_all)):
        with open(path_all[i],'r',encoding='utf8')as f:
            for line in f:
                data.append(json.loads(line))
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
            else:
                break
    else:
        print('Input command error')
def find_data():
    result = 0
    #每一行数据分别存储在了对应的data[]列表中
    #查找用户
    for i in range(0,len(data)):
        data_str = str(data[i])
        if judger ==  1:
            if data_str.find(user) != -1:
                if data_str.find(event) != -1:
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
    print(result)
def run():
    get_cmd()
    read(path)
    find_data()
if __name__ == '__main__':
    run()