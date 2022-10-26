import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="DRRoas64212",
                                  host="node37021-rawiporn.proen.app.ruk-com.cloud",
                                  port="11250",
                                  database="postgres")

    connection.autocommit = True


    cursor = connection.cursor()


    sql = '''CREATE database myHW'''


    cursor.execute(sql)
    print("Database created successfully.......")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:

    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")