import os

filedir=os.path.abspath("文件路径操作1.py") #当前文件的路径
print(filedir)

dir1=os.path.abspath(__file__) #__file==文件路径操作1.py
print(dir1)

dir2=os.path.dirname(dir1) #当前文件路径的上一层路径
print(dir2)

dir3=os.pardir
print(dir3)

filename=os.path.basename("E:\api_test_framework_finish\文件路径操作1.py")
print(filename)