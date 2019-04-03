import conect_mysql

def read_mysql_data():
    cursor = conect_mysql.open_connection().cursor()
    cursor.execute("select * from Customers")
    myresult = cursor.fetchall()
    for result in myresult:
        print(result)

    cursor.close()

read_mysql_data()
