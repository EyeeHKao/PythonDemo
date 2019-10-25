#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='''
    This script is a demo about .txt file IO.
''')
parser.add_argument('filename', help='the filename to be opened')
args = parser.parse_args()
filename = args.filename

#read file(default open with only-read)
f = open(filename)
print(f.read())    #read all content to memory as a string
f.close()

f = open(filename, 'r')
print(f.readline())    #read one line to memory as a string ,pointer go to next line
f.close()

f = open(filename)
print(f.readlines())    #read all lines to memory as a list
f.close()  


#打开文件，循环读入每一行，然后对每一行解析处理
with open(filename, 'r') as f_to_read :
    while True :
        lines = f_to_read.readline()
        if not lines : 
            break

        #To Do处理每一行的内容
	

#以只写文件方式打开，写入数据, 不可读
f_w = open(filename, 'w') #如果文件存在，那么会清空原始文件后开始写,如果不存在，则创建新文件
f_w.write("hello M.R.")   #写到缓存
f_w.flush()               #缓存到磁盘文件
f_w.close()

f_w = open(filename, 'a') #如果文件存在，以追加到文件尾的方式写数据
f_w.write("hello, append")
f_w.flush()
f_w.close()

