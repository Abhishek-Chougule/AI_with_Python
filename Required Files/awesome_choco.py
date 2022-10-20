import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(host="localhost",user="root",password="root",database='awesome_chocolates')
    if conn.is_connected():
        print("Connection Successed :)")
except Error as e:
    print("Connection Failed :(")
    print("Error : ",e)
    
cursor=conn.cursor()

print()
print("---------------------------------------------------------------------")
showtble="SELECT * FROM sales"
cursor.execute(showtble)
record=cursor.fetchall()

for rows in record:
    print("SPID : ",rows[0])
    print("GeoID : ",rows[1])
    print("PID : ",rows[2])
    print("SaleDate : ",rows[3])
    print("Amount : ",rows[4])
    print("Customers : ",rows[5])
    print("Boxes : ",rows[6])
    break;

print()
print("---------------------------------------------------------------------")
query2="select * from awesome_chocolates.sales where SaleDate='2021-01-05'"
cursor.execute(query2)
record=cursor.fetchall()

for rows in record:
    print(rows)

print()
print("---------------------------------------------------------------------")
query2="select SaleDate,Amount,WeekDay(SaleDate) as 'day of week' from awesome_chocolates.sales where WeekDay(SaleDate)=4"
cursor.execute(query2)
record=cursor.fetchall()

for rows in record:
    print(rows)
    break;
    
