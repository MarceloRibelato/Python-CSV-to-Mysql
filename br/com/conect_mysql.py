import MySQLdb

def open_connection():
    mydb = MySQLdb.connect(host='127.0.0.1',
                           user='root',
                           passwd='159753',
                           db='mysql')
    mydb.autocommit(True)
    return mydb




