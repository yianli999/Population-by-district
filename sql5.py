import MySQLdb
import pandas as pd

data =pd.read_csv('各鄉鎮市區人口密度109年.csv',header=1,nrows=370,encoding='utf-8')
#把...改為0，再將整欄型態調整為int
data['年底人口數']=data['年底人口數'].replace('…',0).astype('int')
data['人口密度']=data['人口密度'].replace('…',0).astype('int')


try:
    conn=MySQLdb.connect(host='localhost',
                         user='root',
                         password='xxxxxxxx',
                         database='testdb',
                         port=3306,
                         charset='utf8')
    cursor=conn.cursor()
    #將資料寫入資料庫中
    try:
        for i in range(len(data)):
            sql='''INSERT INTO towndata (year,site,people_total,area,population)
                    VALUE (%s,%s,%s,%s,%s)'''
            var = (data.iloc[i,0],data.iloc[i,1],data.iloc[i,2],data.iloc[i,3],data.iloc[i,4])
            cursor.execute(sql,var)
        conn.commit()
        print('資料寫入完成')
        cursor.close()
        conn.close()
    except Exception as e:
        print('錯誤訊息:',e)
except Exception as e:
    print('資料庫連接失敗',e)
finally:
    print('資料庫連接結束')
    