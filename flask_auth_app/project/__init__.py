import quart.flask_patch
from quart import Quart
from flask_mail import Mail, Message

jays_lsupport_email = 'placeholder@gmail.com'
jays_lsupport_password = '***************'
jays_support_email = 'support@brandname.com'




app = Quart(__name__) 
mail = Mail(app)
app.config['SECRET_KEY']  = 'the1secret2key3is4very5secret6'
app.config['SQLALCHEMY-DATABASE_URI'] = 'sqlite:///db.sqlite'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = jays_lsupport_email
app.config['MAIL_PASSWORD'] = jays_lsupport_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


def send_mail(sender, message):
    msg = Message(
            "message from "+sender,
            sender = jays_lsupport_email,
            recipients = [jays_support_email]
        )
    msg.body = message
    mail.send(msg)




#auth route blueprints
from .auth import auth as auth_blueprint 
app.register_blueprint(auth_blueprint)

#non-auth blueprints
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

    

