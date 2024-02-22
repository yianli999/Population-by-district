import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',
                         user='root',
                         password='xxxxxxxx',
                         database='testdb',
                         port=3306)
    cursor=conn.cursor()
    #建立表格towndata
    sql='''CREATE TABLE if NOT EXISTS towndata(
            year CHAR(4),
            site VARCHAR(20),
            people_total INT(10),
            area FLOAT(10),
            population INT(10))'''
    cursor.execute(sql)
    print('資料表建立完畢')
    
    cursor.close()
    conn.close()
except Exception as e:
    print('資料庫連接失敗',e)
finally:
    print('資料庫連接結束')
