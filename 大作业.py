import random
import string
from pymongo import MongoClient
import  matplotlib.pyplot as plt
import  numpy as np
import  pandas as pd
import  pymongo
#coding=utf-8
#����MongoDB���ݿ�����
client = MongoClient('localhost',27017)

#�����������ݿ�,randΪ���ݿ���
db = client.rand

#�������ü��ϣ�Ҳ��������ͨ����˵�ı�randΪ����
collection = db.rand
collection.remove(None)

#���������������ַ���������ֵ䲢�򼯺��в�������
def Random():
    row = 0
    while row < 1000:
        column = 0
        while column < 100:
            # ����0��100000�������
            integer = random.randint(0, 100000)
            # ����0��100���������
            f = random.uniform(0, 100)
            # ��������ֵ�
            dict1 = {random.choice(string.ascii_letters): random.sample(string.ascii_letters + string.digits, 3)}
            # ��������ַ���
            str1 = ''.join(random.sample(string.ascii_letters + string.digits, 3))
            tuple = (integer, f, dict1, str1)
            yield tuple
            randNum = {
                '����': integer,
                '������': f,
                '�ֵ�': dict1,
                '�ַ���': str1
            }
            collection.insert_one(randNum)
            column += 1
        row += 1
    return 'done'
g = Random()
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()

# scatter ɢ��ͼ

# ��ȡ����
data = pd.DataFrame(list(collection.find()))

# ѡ����Ҫ��ʾ���ֶ�
x = data['����']
y = data['������']
plt.scatter(x, y, c ='b')
plt.show()