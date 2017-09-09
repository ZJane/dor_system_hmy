import pymysql
db=pymysql.connect(host='localhost',port=3306,user='root',db='dor_manage_system',password='1234')
cursor=db.cursor()
cursor.execute("select * from dor")
data=cursor.fetchone()
print(data)
db.close()