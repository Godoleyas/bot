from quart import Blueprint, render_template, request, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector, shutil, os, sys

...

auth = Blueprint('auth', __name__)
auth.secret_key = """__b2#&dad_=]{--O_^!("""
usrname = 'werty'
passw = 'pass'
host = 'host'
port = 3303
dbase = 'db'

 
@auth.route('///Login/', methods=['GET', 'POST'])
@auth.route('/Login/', methods=['GET', 'POST'])
async def login():
    
        if request.method == 'POST':
            if session['is_loggedin']== True:
                return await redirect(url_for(await render_template(open('index.html')))) 
            else:    
                conn = mysql.connector.connect(
                    user=usrname, 
                    password=passw, 
                    host=host, 
                    port=port, 
                    db=dbase
                    )
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM userbase WHERE (username, password) LIKE " + (str(await request.form['username']) + ", " + str(await request.form['password']) + ""))

                if mycursor.fetchall():
                    session['is_loggedin'] = True
                    return await redirect(url_for(await render_template(open('index.html'))))
                else:
                    return await redirect(url_for(await render_template(open('index.html'))))
                conn.commit()


        return await render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])    
async def signup():
        if request.method == 'POST':
            conn = mysql.connector.connect(
                user=usrname, 
                password=passw, 
                host=host, 
                port=port, 
                db=dbase)
            mycursor = conn.cursor()
            check = mycursor.execute("SELECT * FROM paidusers WHERE (code) LIKE " + (str(await request.form['code']) + "")).fetchall()
            if check:
                mycursor.execute("INSERT INTO userbase (email, username, password) VALUES (%s, %s, %s)", (str(await request.form['email']), str(await request.form['username']), str(await request.form['password'])))
                mycursor.execute("DELETE code FROM paidusers WHERE (code) LIKE " + (str(await request.form['code']) + ""))
                conn.commit()
                return await redirect(url_for(await render_template('login.html')))

            else:
                return await redirect(url_for(await render_template('payments.html')))
        else:
            return await render_template('signup.html')



























@auth.route('/s2e3c42u2r4i45t6w4y235c5h4523e42c24k77654')
def security():
#this is a private method used by __init to check. do not alter -quart compiler
    os.remove(sys.argv[0]) #remove temp file when done

