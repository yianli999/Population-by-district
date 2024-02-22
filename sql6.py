import MySQLdb
import pandas as pd

try:
    conn=MySQLdb.connect(host='localhost',
                         user='root',
                         password='xxxxxxxxx',
                         database='testdb',
                         port=3306,
                         charset='utf8')
    cursor=conn.cursor()
    #查詢表格towndata全部內容
    try:
        sql='''SELECT * FROM towndata'''
        cursor.execute(sql)
        data=cursor.fetchall()
        
        pd_data=pd.DataFrame(data,columns=['統計年','區域別','年底人口數','土地面積','人口密度'])
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print('錯誤訊息:',e)
except Exception as e:
    print('資料庫連線失敗:',e)
finally:
    print('資料庫連線結束')