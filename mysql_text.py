import pymysql

db=pymysql.connect(host="localhost",
                   port=3306,
                   user="root",
                   passwd="123456",
                   database='stu',
                   charset='utf8')

cur = db.cursor()
sql="insert into class_2 values('1','小明',15,'m',70)"
cur.execute(sql)
db.commit()
cur.close()
db.close()
