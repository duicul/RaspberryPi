import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="raspberry"
)
def checkdb(dbname,mydatab):
	mycursor=mydatab.cursor()
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
#		print(x)
		if x[0] == dbname:
			return True
	return False
def createdatabase(dbname,mydb):
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE "+dbname)

print(checkdb("raspdb",mydb))
if not checkdb("raspdb",mydb) :
	createdatabase("raspdb",mydb)
print(checkdb("raspdb",mydb))
mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="raspberry",
  database="raspdb"
)
mycursor=mydb.cursor()
try:
	mycursor.execute("CREATE TABLE `pins` ( `Pin_No` int(11) NOT NULL, `Type` varchar(10) NOT NULL,`PID` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	print("Table created")
except :
	print("Table pins create problem (maybe already exists)")

try:
        mycursor.execute("CREATE TABLE `out_pins` (`PID` int(11) NOT NULL,`Value` int(11) NOT NULL) DEFAULT CHARSET=utf8;")
        print("Table created")
except :
        print("Table out_pins create problem (maybe already exists)")


mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)

"CREATE TABLE `out_pins` (`PID` int(11) NOT NULL,`Value` int(11) NOT NULL) DEFAULT CHARSET=utf8;"
