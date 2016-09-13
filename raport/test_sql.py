import pymysql

dbhost = "s62.hekko.net.pl"
dbname = "fmu_pytest"
dbuser = "fmu_pyuser"
dbpass = "x1234y"

# Open database connection
db = pymysql.connect(dbhost,dbuser,dbpass,dbname)

# prepare a cursor object using cursor() method
cursor = db.cursor()


sql = """(SELECT * FROM dbTemp
)"""

# execute SQL query using execute() method.

try: 
	cursor.execute(sql)
except:
	print(pymysql.err.OperationalError)



#Fetch a single row using fetchone() method.
for data in cursor.fetchall():
	print (" " + str(data[1:]))

# disconnect from server
db.close()