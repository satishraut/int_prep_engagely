# can i practice mysql queries here
import mysql.connector as mc
mydb = mc.connect(user='root', password='Minacs@123',
                              host='127.0.0.1', database='python_db',
                              auth_plugin='mysql_native_password') 
cursor = mydb.cursor(buffered=True)
#query = "CREATE DATABASE IF NOT EXISTS python_db"
#query = "CREATE TABLE IF NOT EXISTS my_table(name varchar(255), age int)"
#query = "INSERT INTO my_table (name, age) VALUES ('John', 30),('Satish',34)"
query = "SELECT * FROM my_table;"
cursor.execute(query)

print(cursor.fetchall())
mydb.commit()
cursor.close()
mydb.close()

# now let's connect to the database and execute a query
