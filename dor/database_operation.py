import pymysql
def database_opr(str):
    db = pymysql.connect(host='localhost', port=3306, user='root', db='dormintory_manage_system', password='1234')
    cursor = db.cursor()
    cursor.execute(str)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data