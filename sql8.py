import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt
import sys

# ======================
# 設定中文
# ======================
plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams["font.size"] = 12
plt.rcParams["axes.unicode_minus"] = False

# ======================
# 資料庫連接取得data
# ======================
key = input("請輸入要查詢的縣市名稱：")

try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",     # 主機名稱
                            user="root",        # 帳號
                            password="xxxxxxxxxx", # 密碼
                            database = "testdb", #資料庫
                            port=3306,           # port
                            charset="utf8")      # 資料庫編碼
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    # 查詢表格towndata的全部內容
    try:
        sql = "SELECT * FROM towndata WHERE site LIKE '%s' ORDER BY people_total DESC" %(key+'%')
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) != 0:
            citydata = pd.DataFrame(data, columns=["統計年","區域別","年底人口數","土地面積","人口密度"])
        else:
            print("輸入縣市名有誤")   
            sys.exit(0)
       
    except Exception as e:
        print("錯誤訊息：", e)
 

except Exception as e:
    print("資料庫連接失敗：", e)
    
finally:
    conn.close()
    
# ======================
# 設定畫布
# ======================
# 由縣市總數量決定畫布寬度
if len(data) >= 26:
    plt.figure(figsize=(18,4))
elif len(data) >= 16:
    plt.figure(figsize=(14,4))
else:
    plt.figure(figsize=(10,4))

# ======================
# 繪製圖表
# ======================
# x與y軸
x = [i for i in range(len(citydata))]
y = [citydata.iloc[i,2] for i in range(len(citydata))]

plt.bar(x, y, zorder=10)

# 將x軸更改為區域名
name = [citydata.iloc[i,1][3:] for i in range(len(citydata))]
plt.xticks(x, name, rotation=45)

# 設定標題
plt.title(key + "109年底人口數", size=20)

# 設定網格
plt.grid(axis="y", zorder=0)

plt.show()