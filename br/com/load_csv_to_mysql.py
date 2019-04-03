import conect_mysql
import csv


def insert_data_to_mysql():
    con = conect_mysql.open_connection()
    con.cursor().execute("CREATE TABLE IF NOT EXISTS Customers (names VARCHAR(255), classes VARCHAR(255), mark VARCHAR(255))")

    with open("test.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            con.cursor().execute('INSERT INTO Customers(names, \
                    classes, mark )' \
                    'VALUES("%s", "%s", "%s")',
                    row)

    con.cursor().close()

insert_data_to_mysql()

