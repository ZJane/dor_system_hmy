import pymysql
db=pymysql.connect(host='localhost',port=3306,user='root',db='dormintory_manage_system',password='1234')
cursor=db.cursor()
data=cursor.execute("select * from dor_admin_account")
print(data)
str="insert into dor_admin_account values('2014101020','14myhe','hello123')"
cursor.execute(str)
db.commit()
db.close()
