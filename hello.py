import os
# os.rename("a.txt",'b.txt')
# os.mkdir("text.py")
try:
    fh = open("a.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!第二次写入文件")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()