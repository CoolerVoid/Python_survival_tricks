from wtforms.csrf.core import CSRF
from hashlib import sha512
import datetime

SECRET_KEY = 'justanotherkey!'

class Ice_CSRF(CSRF):
    def deadspread_2minutes(self, min):
       second=min
       if second & 1:
           return min
       else:
           t=datetime.datetime.now() - datetime.timedelta(minutes=1)
	   return t.minute

    def setup_form(self, form):
        self.csrf_context = form.meta.csrf_context
        return super(Ice_CSRF, self).setup_form(form)

    def generate_csrf_token(self, csrf_token):
        now = datetime.datetime.now()
	minutes=str(self.deadspread_2minutes(now.minute))
        token = sha512(SECRET_KEY + self.csrf_context+ minutes).hexdigest()
        return token

    def validate_csrf_token(self, form, field):
        if field.data != field.current_token:
            raise ValueError('Invalid CSRF')
