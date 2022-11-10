import pymysql

Db = pymysql.connect(host='localhost',
                            user='root',
                            password='lani',
                            database='demo1',
                            cursorclass=pymysql.cursors.DictCursor)

cursor=Db.cursor()
query='insert into acc values("nayhi",33)'

try:

    cursor.execute(query)
    Db.commit()
except:
    Db.rollback()

Db.close()
