
# MoneyDatabase
一个金钱数据库

## 能干什么
作为多个数据库的中间件并解决精度问题

<del>（后续支持redis）</del>(已放弃对非传统数据库的支持（无sql语句）)

## 如何安装
```bash
pip install pymoneyd     #如果你的电脑默认使用pip3的话
pip3 install pymoneyd    #如果你的电脑同时安装了py2/3则可能需要这个命令
```

#如何使用
```python
import pymoney

data = pymoney.connect("sqlite", "test.db")#以sqlite3连接数据库
data = pymoney.connect("mysql", "127.0.0.1", 
        "3306", "root", "root", "money")   #以mysql连接数据库

data.init_database()                       #初始化数据库（如果是第一次运行pymoney）
data.new("tetsai")                         #初始化某个用户
data.income("tetsai", "99.99")             #增加某个用户的余额，返回操作后的值
data.expenditure("tetsai", "99.99")        #减少某个用户的余额，返回操作后的值
data.income("tetsai", 134.52)              #增加某个用户的余额，返回操作后的值
data.expenditure("tetsai", 34.51)          #减少某个用户的余额，返回操作后的值
data.transfer("tetsaia", "tetsaib", 10)    #从tetsaia转10元到tetsaib
data.get("tetsai")                         #获取某个用户的余额
data.query_logs("tetsai")                  #查询tetsai用户的日志（包括转入/转出）
data.close()                               #关闭数据库连接
```
income/expenditure/transfer均有日志可循，如果想不记录本次交易，设置参数```nologs=True```即可
