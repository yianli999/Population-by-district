import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',
                          user='root',
                          password='xxxxxxx',
                          port=3306)
    cursor =conn.cursor()
    #查詢所有資料庫
    sql='''SHOW DATABASES'''
    cursor.execute(sql)
    
    for db in cursor:
        print(db)
    cursor.close()
    conn.close()
    
except Exception as e:
    print('資料庫連接失敗',e)
    
finally:
    print('資料庫連接結束')

