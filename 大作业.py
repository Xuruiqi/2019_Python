import string
import random
from pymongo import MongoClient
import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 


#1.���ӱ������ݿ����
name = MongoClient('localhost')
#2.���ӱ������ݿ� demo û�лᴴ��
db = name.mapx#demo���ݿ���
#3.���������Ӽ���
emp = db.pxm #��������
emp.remove(None)
def generateRandomNumber(i):
    while i!=0:
        Int=random.randint(1,100000)
        Float=random.random()
        Char=random.choice('ud7hfji8jkgikgjksdjgshjgdsgjgdsjjkdkdgsjkgdsgdjdsghgdsgdjskjdgsjkdgkgd')
        Str=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(Int):Str}
        lop=(Int,Float,Char,Str,dict)
        yield lop
        randomNumber = {
            '����': Int,
            '������':Float,
            '�ַ�': Char,
            '�ֵ�': dict,
            '�ַ���':Str
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("mpx.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()

 emp = db['pxm']
# ��ȡ����
y = data['����']
# ѡ����Ҫͳ�Ƶ��ֶ�



fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x=np.arange(1,100001) 
ax.scatter(x,y,c='green')
ax.legend('int') 
ax.grid(True)
plt.show()