from database.database import Database


print ("\nTest crud agenda\n")

db = Database()
db.InsertUser("Test1","22","23","13371337")
db.InsertUser("Test2","23","1337","13371337")
db.InsertUser("Test3","24","1337","13371337")
db.InsertUser("Test4","25","1337","13371337")

# elements name, age, weight, cell
table=db.GetAllUsers()

for user in table:
 print(user.name)


#if db:
# db.close();

