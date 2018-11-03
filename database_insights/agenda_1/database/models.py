from pydal import DAL, Field

class models(object):
    def __new__(self,):
        dalString  = 'sqlite://Agenda.db'  
        db = DAL(dalString,migrate=True)
        db.define_table('users',
            Field('name','string',unique=True),
            Field('age','integer'),
            Field('weight','string'),
            Field('cell','string'),
            Field('id', type='id')
	    )
        return db


# study that doc for more info http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#insert

