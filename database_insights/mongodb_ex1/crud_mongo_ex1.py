# Example with CRUD by @CoolerVoid
# this is a simple PoC to test MongoDB with Python3
import flask
from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine.queryset.visitor import Q 

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'admin',
    'host': '127.0.0.1',
    'port': 27017,
    'username': 'root',     
    'password': 'Presto2'
}

db = MongoEngine()
db.init_app(app)

# Study this stuff to understand each step http://docs.mongoengine.org/guide/querying.html#default-document-queries

# simple model
class users_zoltar(db.Document):
    login = db.StringField(required=True,primarykey="True", max_length=200)
    hashpass = db.StringField(required=True,max_length=500)


######## Insert user examples

# test if user exist
test = users_zoltar.objects(login__exact='Melfolk').count()
#if not exist create him
if test == 0:
    post1 = users_zoltar(login='Melfolk', hashpass='water').save()
# test if user exist
test = users_zoltar.objects(login__exact='japan1987').count()
#if not exist create him
if test == 0:
    post1 = users_zoltar(login='japan1987', hashpass='ultraman').save()
# test if user exist
test = users_zoltar.objects(login__exact='kamenrider').count()
#if not exist create him
if test == 0:
    post1 = users_zoltar(login='kamenrider', hashpass='black').save()


####### Show all documents of user_zoltar collection...
for post in users_zoltar.objects:
    print(str(post.login)+" "+str(post.hashpass))

print("\nEnd first wave of tests\n")

##### Update row element example

post2=users_zoltar.objects(login='kamenrider').first()
post2=post2.update(set__hashpass='white')

###### Delete User example
rm=users_zoltar.objects(login='japan1987').delete()

####### Show all documents of user_zoltar collection...
for post in users_zoltar.objects:
    print(str(post.login)+" "+str(post.hashpass))


####### Example query to simulate auth
print("\n Try auth:")
authtest = users_zoltar.objects( Q(login__exact='Melfolk') & Q(hashpass__exact='water') ).count()
if authtest == 1:
    print("Login ok")
else:
    print("Login not ok")    


## TODO add paginate examples...

## TODO add cascade examples....
