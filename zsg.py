"""
增删改练习
"""
import pymysql
#嘤嘤嘤
#创建链接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()
while True:
    name = input('name:')
    age = input('age:')
    gender = input('m or w:')
    score = input('score:')

    # sql = "insert into myclass(name,ahe,gender,score) values('%s',%d,'%s',%f)"%(name,age,gender,score)
    sql = "insert into myclass(name,ahe,gender,score) " \
          "values(%s,%s,%s,%s);"

    try:
        cur.execute(sql,[name,age,gender,score])
        db.commit()
    except Exception as e:
        db.rollback()
        print('faild',e)
cur.close()
db.close()




