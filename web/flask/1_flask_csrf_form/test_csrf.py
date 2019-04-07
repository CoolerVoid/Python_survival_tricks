from helper import tokenform
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class TheForm(Form):
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

    class Meta:
        csrf = True
        csrf_class = tokenform.Ice_CSRF
 
 
@app.route("/", methods=['GET', 'POST'])
def index():
    form = TheForm(
      request.form,
      meta={'csrf_context': request.remote_addr }
    )
    print form.errors

    if request.method == 'POST':
        password=request.form['password']
        email=request.form['email']
	token=request.form['csrf_token']
        print "::DEBUG::"
        print  "Email:",email, " Pass:", password, "Token:",token
 
        if form.validate():
            if password == "qwerty":
                flash('Welcome ! ' + email)
            if form.csrf_token.errors: 
                flash('Error: form token invalid try to post again')
        else:
            flash('Error: All the form fields are required. ')
    return render_template('template.html', form=form)
 
if __name__ == "__main__":
    app.run()
