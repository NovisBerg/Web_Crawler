# pip3 install pymysql
import pymysql


# 建立链接
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='shengmin321',
    db='gwent',
    use_unicode = True,
    charset='utf8'
)

