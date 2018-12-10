import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'vminformdev01' 
database = 'GI_VS_SC_Test' 

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM FOO;") 
results = cursor.fetchall() 

for row in results:
    print(row)

cnxn.close()
