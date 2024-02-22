import MySQLdb

try:
    #開啟資料庫連結
    conn= MySQLdb.connect(host='localhost',
                          user='root',
                          password='xxxxxxx',
                          port=3306)
    #使用cursor()操控資料庫
    cursor=conn.cursor()
    #查詢資料庫版本
    cursor.execute("SELECT @@version")
    db_info=cursor.fetchone()
    print('資料庫版本:%s'%(db_info))
    
    #查詢資料庫字元集
    cursor.execute("SELECT @@character_set_database,@@collection_database")
    db_character=cursor.fetchall()
    print('字元集為%s'%db_character)
    
    cursor.close()
    conn.close()

except Exception as e:
    print('資料庫連接失敗',e)
finally:
    print('資料庫連線結束')
    
    