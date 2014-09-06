#! python3
import sqlite3

conn = sqlite3.connect("aaa.sqlite")

# 这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
conn.isolation_level = None

# 下面就是创建一个表
try:
    conn.execute(
        "create table if not exists t1(id integer primary key autoincrement, name varchar(128), info varchar(128),a varchar(30),b varchar(30),c varchar(30))")
except:
    print('数据库已经存在')

# 插入数据
aa = '啦啦啦'
for t in(('2006-03-28', 'BUY', 'IBM', 1000, 45.00), ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00), ('2006-04-06', 'SELL', 'IBM', 500, 53.00)):
    conn.execute("insert into t1(name,info,a,b,c) values (?,?,?,?,?)", t)

# 如果隔离级别不是自动提交就需要手动执行commit

# conn.commit()

# 获取到游标对象

cur = conn.cursor()

# 用游标来查询就可以获取到结果

cur.execute("select name from t1")

# 获取所有结果

res = cur.fetchall()

print(res)

# cur.description是对这个表结构的描述
cur.execute("select id from t1 where c>45")
ss = cur.fetchall()
print(ss)

cur.close()

conn.close()
