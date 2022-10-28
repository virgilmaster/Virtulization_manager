import os
import datetime
import sys
from subprocess import call
# import flask
# import win32api


# 然后有一个交互式体验的程序 
# 有对话框 
# 提示信息
# 然后设计一个图标
# 可以一键部署

# Not a wonderful function:
# def check_type(docker_file,docker_name):
#     if type(docker_file) == str:
#         print("It's correct")
#     elif type(docker_file) == int:
#         print("have something wrong")
#         sys.exit
#     elif type(docker_file) == float:
#         print("have something wrong")
#         sys.exit
#     if type(docker_name) == str:
#         print("It's correct")
#     elif type(docker_name) == int:
#         print("have something wrong")
#         sys.exit
#     elif type(docker_name) == float:
#         print("have something wrong")
#         sys.exit


# 想做一个自动进入容器里然后把想要找的文件以find / -name 找出来 然后再拷贝出来
def copy_file(docker_name,docker_file,save_path):
    start_dockercompose = call("XXXXX")
    # launch the container function have finished
    if docker_name == 'kali':
        print('Start the hacker container now!!!')
        os.system("docker start XXXXX")
    elif docker_name == 'centos':
        print('Start the normal container now!!!')
        os.system("docker start XXXXX")
    else:
        print('My lord you have wrong name,plz check again ~。~')
    while docker_name == 'kali':
        os.system('docker cp XXXXX:' + docker_file + save_path)
        print('My lord i have achieve the files from the container')
    else:
        os.system('docker cp XXXXX:' + docker_file + save_path)
        print('My lord i have achieve the files from the container')



if __name__ == '__main__':
    # Have problem not a wonderful function
    docker_file = input("My lord plz enter the document's files you want search: ")
    docker_name = input('My lord plz enter which container you want in: ')
    save_path = r'XXXXXX'
    print('Current time is: ', datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    # check_type(docker_file,docker_name)
    copy_file(docker_name,docker_file,save_path)
