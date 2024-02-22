import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',
                         user='root',
                         password='xxxxxxxx',
                         database='testdb',
                         port=3306,
                         charset='utf8')
    cursor=conn.cursor()
    #查詢表格towndata的指定縣市資料
    key = input('請輸入要查詢的縣市名:')
    try:
        sql="SELECT site,people_total FROM towndata WHERE site LIKE '%s'"%(key+'%')
        cursor.execute(sql)
        data=cursor.fetchall()
        
        for i in data:
            print(i)
        print("%s一共有%d筆資料"%(key,len(data)))
              
        cursor.close()
        conn.close()
    except Exception as e:
        print('錯誤資訊:',e)
except Exception as e:
    print('資料庫連接失敗:',e)
finally:
    print('資料庫連線結束')
    
    
    