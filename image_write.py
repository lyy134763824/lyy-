import pymysql

db=pymysql.connect(host="localhost",
                   port=3306,
                   user="root",
                   passwd="123456",
                   database='stu',
                   charset='utf8')
#获取游标
cur = db.cursor()
with open("hexi.jpeg","rb") as f:
    data=f.read()


try:
    sql="insert into class_2 values(4,'鹤熙',10,'w',100,%s)"
    cur.execute(sql,[data])
    db.commit()
except Exception as e:
    db.rollback()#让数据酷返回之前的状态
    print(e)
cur.close()
db.close()

