import string
import random
from pymongo import MongoClient

#1.���ӱ������ݿ����
name = MongoClient('localhost')
#2.���ӱ������ݿ� demo û�лᴴ��
db = name.xcnhr  #demo���ݿ���
#3.���������Ӽ���
emp = db.mydb #��������
emp.remove(None)

def generateRandomNumber(i):
    while i!=0:
        randomInt=random.randint(1,100000)
        randomFloat=random.random()
        randomChar=random.choice('hhcsbxiaguosbfhdjfdjfdshfdkjfkjfdfjkfkjhfdskjfdioefiofeiifeiofiiefsiojfseioj')
        randomStr=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(randomInt):randomStr}
        tup1=(randomInt,randomFloat,randomChar,randomStr,dict)
        yield tup1
        randomNumber = {
            '����': randomInt,
            '������':randomFloat,
            '�ַ�': randomChar,
            '�ֵ�': dict,
            '�ַ���':randomStr
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("xcnhr.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
#for i in emp.find():
 # print(i)