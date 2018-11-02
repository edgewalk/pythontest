# # 导入MySQL驱动:
import pymysql
if __name__ == '__main__':
    #连接配置信息
    config = {
        'host':'127.0.0.1',
        'port':3306,#MySQL默认端口
        'user':'root',#mysql默认用户名
        'password':'jianghui1992',
        'db':'test',#数据库
        'charset':'utf8'
    }
    # 获取一个数据库连接
    with pymysql.connect(**config) as conn:
        print("connect database successfully")
        cursor = conn.cursor()

        # 创建一个游标对象 cursor
        # with  conn.cursor() as cur:
        #     pass
            # 使用 execute()  方法执行 SQL 查询
            # cur.execute("SELECT VERSION()")
            # # 使用 fetchone() 方法获取单条数据.
            # data = cur.fetchone()
            # print ("Database version : %s " % data)
if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect("localhost","root","jianghui1992","test" )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print ("Database version : %s " % data)

    # 关闭数据库连接
    db.close()

