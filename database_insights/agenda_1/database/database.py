import time
from database.models import models

class Database(object):
    def InsertUser(self,name0,age0,weight0,cell0):
     try:
      db = models()
      db.users.insert(name=name0,age=age0,weight=weight0,cell=cell0)
      db.commit()
     except Exception as error:
      print (error)
     finally:
      if db:
       db.close() 

    def UpdateUser(self,name0,age0,weight0,cell0):
     try:
      db = models()
      db.users.update_or_insert(name=name0,age=age0,weight=weight0,cell=cell0)
      db.commit()
     except Exception as error:
      print (error)
     finally:
      if db:
       db.close() 

    def GetAllUsers(self,):
     try:
      db = models()
      results = db().select(db.users.ALL,orderby=~db.users.id)
     except Exception as error:
      print (error)
      return error
     finally:
      if db:
       db.close() 
      return results

    def DeleteUserByName(self,name):
     try:
      db = models()
      db(db.blacklists.name == name).delete()
      db.commit()
     except Exception as error:
      print (error)
     finally:
      if db:
       db.close() 

    def CheckUserExist(self,host,url):
     try:
      db = models()
      result = db(db.users.name == name).select()
      return len(result)
     except Exception as error:
      print (error)
      return error
     finally:
      if db:
       db.close() 

