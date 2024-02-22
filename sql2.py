import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',
                          user='root',
                          password='xxxxxxx',
                          port=3306)
    cursor =conn.cursor()
    #創建資料庫testdb
    sql = '''CREATE DATABASE IF NOT EXISTS testdb
             CHARACTER SET UTF8MB4
             COLLATE utf8mb4_0900_ai_ci'''
    cursor.execute(sql)
    
    print('資料庫創建成功')
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print('資料庫連接失敗',e)
finally:
    print('資料庫連線結束')