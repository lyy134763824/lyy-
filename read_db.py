import pymysql
import re
# db=pymysql.connect(host="localhost",
#                    port=3306,
#                    user="root",
#                    passwd="123456",
#                    database='stu',
#                    charset='utf8')
#获取游标
#cur = db.cursor()
#sql="select * from sanguo where gender='男';"
# sql="select name,age from sanguo where gender='男';"
# #执行正确后调用cur函数获取结果
# cur.execute(sql)
# #获取一个结果
# # one_row=cur.fetchone()
# # print(one_row[1])#元祖
# # many_row=cur.fetchmany(2)
# print(many_row)#元祖桃源组
# cur.close()
# db.close()
with open("dict.txt") as f:
    for line in f:
        if line == "\n":
            break
        temp = re.findall(r"(\S+)\s+(.*)",line)[0]
        word=temp[0]
        exp=temp[1]












#关闭数据库
# db.close()
# cur.close()




