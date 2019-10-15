import time
import random
import datetime
import json
import uuid
import sys
print(sys.argv)
print(uuid.uuid1())
# print(uuid.uuid3())
print(random.randint(1,10))
print(time.ctime(time.time()))
print(int(time.time()))
date=int(time.time())-7*24*60*60#计算七天前的时间
print(date)
print(time.localtime(date))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(date)))
print(time.localtime(time.time()))

print(datetime.datetime.now())

now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(now)

file=open("waf_example.txt")
f=file.readlines()
file.close()

for item in f:
    print(item.strip("\n"))
    newdict=json.loads(item)
    print(newdict)

a=3
print(isinstance(a,int))
