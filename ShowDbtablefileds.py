import pymysql

Db = pymysql.connect(host='localhost',
                            user='root',
                            password='lani',
                            database='demo2')
                            #cursorclass=pymysql.cursors.DictCursor)
with Db.cursor() as cursor:
    sql="select * from student"
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
