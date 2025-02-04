import string
import random
from pymongo import MongoClient

#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库 demo 没有会创建
db = name.random_number   #demo数据库名
#3.创建，连接集合
emp = db.myrandom  #集合名字
emp.remove(None)

def Random(k):
    c=0
    while k!=0:
        c+=1
        wuli=random.randint(1,10)
        ran_str =  ''.join(random.sample(string.ascii_letters + string.digits,wuli))
        leo=random.uniform(1,10)
        m=random.randint(1,100000)
        n=random.choice(string.ascii_letters)
        dicta={n:leo}
        dictb={n:m}
        dictc={n:ran_str}
        c1=(str(c)+':')
        tup1 = (c1,ran_str,leo,m,dicta,dictb,dictc)
        yield tup1
        randomNumber = {
            '序号':c,
            '整型': m,
            '浮点数':leo,
            '字符': ran_str,
            '字典1': dicta,
            '字典2':dictb,
            '字典3':dictc
        }
        emp.insert_one(randomNumber)
        k= k - 1
    return 'done'
g = Random(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()

# 读取数据
data = pd.DataFrame(list(table.find()))
y = data['整型']
z = data['浮点数']


fig = plt.figure()  
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_title('Scatter int') 
ax2.set_title('Scatter folat')
ax1.scatter(x,y,c = 'g',marker = 'o')
ax2.scatter(x,z,c = 'b',marker = 'x')
plt.show()
)