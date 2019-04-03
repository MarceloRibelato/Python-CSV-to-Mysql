import conect_mysql

def drop_table():
    cursor = conect_mysql.open_connection().cursor()
    cursor.execute("DROP TABLE Customers")
    cursor.close()
    print "Table Dropped"

drop_table()
